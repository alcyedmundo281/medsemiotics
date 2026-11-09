"""Identidad y créditos de los autores de Medsemiotics."""

from __future__ import annotations

import re
from datetime import date
from typing import Annotated, Literal, Self

from pydantic import BaseModel, ConfigDict, Field, StringConstraints, model_validator

Texto = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]

RolObra = Literal["autor-fundador", "autor", "coordinacion-editorial", "autor-autoevaluaciones"]
# Taxonomía CRediT (NISO Z39.104-2022), en las claves en español que usa biosemiotics.
CreditRol = Literal[
    "conceptualizacion",
    "curacion-de-datos",
    "analisis-formal",
    "adquisicion-de-fondos",
    "investigacion",
    "metodologia",
    "administracion-del-proyecto",
    "recursos",
    "software",
    "supervision",
    "validacion",
    "visualizacion",
    "redaccion",
    "revision-edicion",
]

# Roles que un autor fallecido no puede ejercer sobre la edición nueva.
ROLES_SOLO_VIVOS: frozenset[str] = frozenset(
    {"revision-edicion", "supervision", "validacion", "administracion-del-proyecto"}
)

# Un revisor es una persona nominada. Nombres de agentes o modelos no cuentan.
AGENTES = re.compile(r"\b(claude|codex|copilot|gpt|chatgpt|gemini|llm|ia|ai|agente)\b", re.I)

ORCID = re.compile(r"^\d{4}-\d{4}-\d{4}-\d{3}[\dX]$")


def orcid_valido(orcid: str) -> bool:
    """Formato y dígito de control ISO 7064 MOD 11-2, como lo calcula ORCID."""
    if not ORCID.match(orcid):
        return False
    digitos = orcid.replace("-", "")
    total = 0
    for caracter in digitos[:-1]:
        total = (total + int(caracter)) * 2
    resto = (12 - total % 11) % 11
    control = "X" if resto == 10 else str(resto)
    return digitos[-1] == control


class _Base(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class Autor(_Base):
    nombre: Texto
    orcid: str | None = None
    afiliacion: Texto | None = None
    # Forma con la que la persona firma en la bibliografía (p. ej. «Alcy R. Torres», PubMed:
    # «Torres AR»): se usa en la línea de revisión y en las citas. La portada usa `nombre`.
    nombre_bibliografico: Texto | None = None
    rol_obra: RolObra = "autor"
    fallecido: bool = False
    # Fechas de vida (ISO) de quien las lleva en un paratexto (la dedicatoria). No viajan a los
    # JSON derivados de los casos.
    nacimiento: date | None = Field(default=None, exclude=True)
    fallecimiento: date | None = Field(default=None, exclude=True)
    # Concordancia de género de su función en créditos («autora»): lo dice el mapa, no se deduce
    # del nombre.
    femenino: bool = Field(default=False, exclude=True)
    credit: list[CreditRol] = Field(min_length=1)

    @model_validator(mode="after")
    def _coherencia(self) -> Self:
        if self.orcid is not None and not orcid_valido(self.orcid):
            raise ValueError(f"ORCID inválido para {self.nombre}: {self.orcid}")
        if self.fallecimiento is not None:
            if not self.fallecido:
                raise ValueError(f"{self.nombre}: tiene fecha de fallecimiento pero no fallecido")
            if self.nacimiento is not None and self.nacimiento >= self.fallecimiento:
                raise ValueError(f"{self.nombre}: nace después de fallecer")
        if self.fallecido:
            prohibidos = sorted(ROLES_SOLO_VIVOS.intersection(self.credit))
            if prohibidos:
                raise ValueError(
                    f"{self.nombre} (fallecido) no puede ejercer en esta edición: "
                    + ", ".join(prohibidos)
                )
        return self
