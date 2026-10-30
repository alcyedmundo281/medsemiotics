"""Esquema de ``classroom/curso-*.yaml``: el sílabo como datos."""

from __future__ import annotations

from datetime import date
from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field, StringConstraints

Texto = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
HmId = Annotated[str, StringConstraints(pattern=r"^HM:\d+$")]


class _Base(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class Curso(_Base):
    nombre: Texto
    seccion: Texto
    descripcion: Texto
    zona_horaria: Texto
    hora_inicio: Annotated[str, StringConstraints(pattern=r"^\d{2}:\d{2}$")]
    duracion_min: int = Field(gt=0)
    base_url: Texto
    classroom_url: Texto | None = None
    silabo_pdf: Texto | None = None
    recesos: list[date]


class Unidad(_Base):
    id: Texto
    titulo: Texto


class Sesion(_Base):
    n: int = Field(ge=1)
    fecha: date
    unidad: Texto
    tema: Texto
    condiciones: list[HmId]
    recursos: list[Texto]
    evaluacion: Literal["sumativa_1", "sumativa_final"] | None = None


class Componente(_Base):
    id: Texto
    titulo: Texto
    peso: int = Field(ge=0, le=100)
    sesion: int | None = None


class Criterio(_Base):
    titulo: Texto
    puntos: int = Field(gt=0)


class Rubrica(_Base):
    id: Texto
    titulo: Texto
    criterios: list[Criterio]


class Tarea(_Base):
    id: Texto
    titulo: Texto
    componente: Texto
    rubrica: Texto | None = None
    sesion_publicacion: int
    sesion_entrega: int
    propuesta: bool = False


class Plan(_Base):
    curso: Curso
    unidades: list[Unidad]
    sesiones: list[Sesion]
    componentes: list[Componente]
    rubricas: list[Rubrica]
    tareas: list[Tarea]
