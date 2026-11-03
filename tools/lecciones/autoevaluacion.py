"""Autoevaluaciones: ``lecciones/autoevaluaciones/<id-de-la-leccion>.yaml``.

Una autoevaluación es el banco de preguntas de una lección. Su fuente única es el YAML; el
contenido de las preguntas es de la autora y esta validación no lo juzga: comprueba la forma y el
contrato editorial.

- La lección existe, y el archivo se llama como ella.
- Autores y revisor son claves de ``lecciones/mapa.yaml`` y coinciden con su sección
  ``autoevaluaciones``.
- Cada pregunta tiene cuatro opciones (A-D) distintas y una sola correcta.
- Las cifras de rendimiento diagnóstico entran solo por token, y todo token resuelve contra la
  evidencia a una revisión fijada. Una cifra de datos del paciente («38 semanas») no exige cita.
- ``revisado`` requiere un revisor humano nominado en el mapa y una fecha; un agente nunca lo es.
"""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, Annotated, Literal, Self

import yaml
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    StringConstraints,
    ValidationError,
    model_validator,
)

from lecciones.fuente import ErrorDeFuente, leer
from lecciones.modelo import AGENTES, Leccion, UsoIA
from lecciones.tokens import problemas_de_tokens
from lecciones.validacion import problemas_de_evidencia

if TYPE_CHECKING:
    from collections.abc import Mapping
    from pathlib import Path

    from casos.articulo import Articulo
    from lecciones.mapa import Mapa

Texto = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
Letra = Literal["A", "B", "C", "D"]
LETRAS: tuple[str, ...] = ("A", "B", "C", "D")
Nivel = Literal["recordar", "comprender", "aplicar", "analizar", "evidencia"]
EstadoAutoevaluacion = Literal["borrador", "revisado"]
CARPETA_AUTOEVALUACIONES = ("lecciones", "autoevaluaciones")


class _Base(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class Pregunta(_Base):
    id: Annotated[str, StringConstraints(pattern=r"^p\d{2}$")]
    nivel: Nivel
    seccion: Texto
    enunciado: Texto
    opciones: dict[Letra, Texto]
    correcta: Letra
    explicacion: Texto

    @model_validator(mode="after")
    def _opciones(self) -> Self:
        if tuple(sorted(self.opciones)) != LETRAS:
            raise ValueError(f"{self.id}: debe tener exactamente las opciones A, B, C y D")
        if len({" ".join(t.lower().split()) for t in self.opciones.values()}) != len(LETRAS):
            raise ValueError(f"{self.id}: dos opciones dicen lo mismo")
        return self

    def textos(self) -> list[tuple[str, str]]:
        """Pares (campo, texto) con prosa de la pregunta."""
        return [
            ("enunciado", self.enunciado),
            *((f"opción {letra}", texto) for letra, texto in sorted(self.opciones.items())),
            ("explicación", self.explicacion),
        ]


class Autoevaluacion(_Base):
    leccion: Annotated[str, StringConstraints(pattern=r"^leccion-[a-z0-9]+(-[a-z0-9]+)*$")]
    estado: EstadoAutoevaluacion
    autores: list[Texto] = Field(min_length=1)
    revisor: Texto | None = None
    fecha_revision: date | None = None
    uso_ia: list[UsoIA]
    documento_de_trabajo: Texto | None = None
    preguntas: list[Pregunta] = Field(min_length=1)
    pendientes: list[Texto] = Field(default_factory=list)

    @model_validator(mode="after")
    def _contrato(self) -> Self:
        ids = [p.id for p in self.preguntas]
        if len(set(ids)) != len(ids):
            raise ValueError("preguntas: id repetido")
        if len(set(self.autores)) != len(self.autores):
            raise ValueError("autores: hay valores repetidos")
        if self.revisor is not None and AGENTES.search(self.revisor):
            raise ValueError("revisor: debe ser una persona; el agente nunca es revisor")
        if self.estado == "revisado":
            if self.revisor is None:
                raise ValueError("estado revisado: requiere un revisor nominado")
            if self.fecha_revision is None:
                raise ValueError("estado revisado: requiere fecha_revision")
        return self


def rutas(raiz: Path) -> list[Path]:
    carpeta = raiz.joinpath(*CARPETA_AUTOEVALUACIONES)
    return sorted(carpeta.glob("*.yaml")) if carpeta.is_dir() else []


def problemas_de_datos(
    nombre: str,
    datos: object,
    mapa: Mapa,
    lecciones: Mapping[str, Leccion | None],
    articulos: Mapping[str, Articulo],
) -> list[str]:
    """Todos los problemas de una autoevaluación ya leída; ``nombre`` es el del archivo."""
    if not isinstance(datos, dict):
        return [f"{nombre}: debe ser un diccionario YAML"]
    try:
        banco = Autoevaluacion.model_validate(datos)
    except ValidationError as exc:
        return [
            f"{nombre}: {'.'.join(str(p) for p in e['loc']) or 'archivo'}: {e['msg']}"
            for e in exc.errors()
        ]

    problemas: list[str] = []
    if nombre != f"{banco.leccion}.yaml":
        problemas.append(f"{nombre}: el archivo debe llamarse {banco.leccion}.yaml")
    if banco.leccion not in lecciones:
        problemas.append(f"{nombre}: la lección {banco.leccion} no existe en lecciones/")

    problemas += _problemas_de_autoria(nombre, banco, mapa)

    leccion = lecciones.get(banco.leccion)
    for pregunta in banco.preguntas:
        for campo, texto in pregunta.textos():
            donde = f"{nombre}: {pregunta.id} {campo}"
            # Sin exigir cita: una cifra de datos del paciente («38 semanas») no es evidencia.
            problemas += [f"{donde}: {p}" for p in problemas_de_evidencia(texto, leccion, False)]
            declaradas = leccion.condiciones if leccion is not None else []
            problemas += [
                f"{donde}: {p}" for p in problemas_de_tokens(texto, declaradas, articulos)
            ]
    return problemas


def _problemas_de_autoria(nombre: str, banco: Autoevaluacion, mapa: Mapa) -> list[str]:
    problemas: list[str] = []
    cfg = mapa.autoevaluaciones
    if cfg is None:
        return [f"{nombre}: lecciones/mapa.yaml no declara «autoevaluaciones»"]
    for clave in banco.autores:
        if clave not in mapa.personas:
            problemas.append(f"{nombre}: autores: «{clave}» no está en lecciones/mapa.yaml")
        elif clave not in cfg.autores:
            problemas.append(
                f"{nombre}: autores: «{clave}» no figura entre los autores de las "
                "autoevaluaciones del mapa"
            )
    if banco.revisor is not None:
        if banco.revisor not in mapa.personas:
            problemas.append(f"{nombre}: revisor: «{banco.revisor}» no está en lecciones/mapa.yaml")
        elif banco.revisor != cfg.revisor:
            problemas.append(
                f"{nombre}: revisor: «{banco.revisor}» no es el revisor de las autoevaluaciones "
                f"del mapa («{cfg.revisor}»)"
            )
    return problemas


def problemas_de_autoevaluaciones(
    raiz: Path,
    mapa: Mapa,
    lecciones: Mapping[str, Leccion | None],
    articulos: Mapping[str, Articulo] | None,
) -> list[str]:
    """Problemas de todos los ``lecciones/autoevaluaciones/*.yaml`` (``lecciones check``)."""
    problemas: list[str] = []
    for ruta in rutas(raiz):
        try:
            datos = yaml.safe_load(ruta.read_text(encoding="utf-8"))
        except yaml.YAMLError as exc:
            problemas.append(f"{ruta.name}: YAML inválido: {exc}")
            continue
        problemas += problemas_de_datos(ruta.name, datos, mapa, lecciones, articulos or {})
    return problemas


def lecciones_por_id(rutas_qmd: list[Path]) -> dict[str, Leccion | None]:
    """Cada lección del repositorio por su id (el nombre del archivo); ``None`` si no valida."""
    salida: dict[str, Leccion | None] = {}
    for ruta in rutas_qmd:
        try:
            salida[ruta.stem] = Leccion.model_validate(leer(ruta).datos)
        except (ErrorDeFuente, ValidationError):
            salida[ruta.stem] = None
    return salida
