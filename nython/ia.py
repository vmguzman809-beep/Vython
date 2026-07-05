"""Integracion opcional de IA para Nython."""

from __future__ import annotations

import os
from pathlib import Path

from .traductor import traducir_codigo
from .utilidades import leer_archivo_nython


MODELO_PREDETERMINADO = "gpt-5.5"

INSTRUCCIONES_BASE = (
    "Eres el asistente educativo integrado de Nython. Responde en espanol claro, "
    "con ejemplos pequenos, y ayuda a estudiantes a entender Python y Nython."
)


class NythonIAError(RuntimeError):
    """Error de configuracion o ejecucion de la capa IA."""


def ia_disponible() -> bool:
    """Indica si hay una API key configurada para usar IA."""

    return bool(os.getenv("OPENAI_API_KEY"))


def preguntar_ia(
    pregunta: str,
    *,
    instrucciones: str = INSTRUCCIONES_BASE,
    modelo: str | None = None,
) -> str:
    """Pregunta a un modelo de IA usando la API de OpenAI.

    Requiere instalar el extra `ia` y definir la variable `OPENAI_API_KEY`.
    """

    if not os.getenv("OPENAI_API_KEY"):
        raise NythonIAError(
            "Falta OPENAI_API_KEY. Configura tu clave o usa funciones de Nython sin IA."
        )

    try:
        from openai import OpenAI
    except ImportError as exc:
        raise NythonIAError("Falta instalar el extra de IA. Ejecuta: pip install -e .[ia]") from exc

    client = OpenAI()
    respuesta = client.responses.create(
        model=modelo or os.getenv("NYTHON_IA_MODELO", MODELO_PREDETERMINADO),
        instructions=instrucciones,
        input=pregunta,
    )
    return respuesta.output_text


def crear_prompt_explicacion(codigo_nython: str, codigo_python: str) -> str:
    return "\n".join(
        [
            "Explica este programa Nython para una persona principiante.",
            "Incluye que hace cada bloque y muestra la relacion con Python.",
            "",
            "Codigo Nython:",
            "```nython",
            codigo_nython,
            "```",
            "",
            "Python generado:",
            "```python",
            codigo_python,
            "```",
        ]
    )


def crear_prompt_revision(codigo_nython: str, codigo_python: str) -> str:
    return "\n".join(
        [
            "Revisa este programa Nython como tutor.",
            "Busca errores, mejoras de claridad y oportunidades de aprendizaje.",
            "No cambies el objetivo del programa.",
            "",
            "Codigo Nython:",
            "```nython",
            codigo_nython,
            "```",
            "",
            "Python generado:",
            "```python",
            codigo_python,
            "```",
        ]
    )


def explicar_archivo(ruta: str | Path, *, modelo: str | None = None) -> str:
    codigo_nython = leer_archivo_nython(ruta)
    codigo_python = traducir_codigo(codigo_nython)
    return preguntar_ia(crear_prompt_explicacion(codigo_nython, codigo_python), modelo=modelo)


def revisar_archivo(ruta: str | Path, *, modelo: str | None = None) -> str:
    codigo_nython = leer_archivo_nython(ruta)
    codigo_python = traducir_codigo(codigo_nython)
    return preguntar_ia(crear_prompt_revision(codigo_nython, codigo_python), modelo=modelo)
