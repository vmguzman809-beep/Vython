"""Integracion opcional de IA para Nython."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol

from .traductor import traducir_codigo
from .utilidades import leer_archivo_nython


MODELO_PREDETERMINADO = "gpt-5.5"
PROVEEDOR_PREDETERMINADO = "openai"

INSTRUCCIONES_BASE = (
    "Eres el asistente educativo integrado de Nython. Responde en espanol claro, "
    "con ejemplos pequenos, y ayuda a estudiantes a entender Python y Nython."
)


class NythonIAError(RuntimeError):
    """Error de configuracion o ejecucion de la capa IA."""


class ProveedorIA(Protocol):
    nombre: str

    def generar(self, prompt: str, *, instrucciones: str, modelo: str) -> str:
        """Genera texto a partir de un prompt."""


@dataclass(frozen=True)
class ConfiguracionIA:
    proveedor: str = PROVEEDOR_PREDETERMINADO
    modelo: str = MODELO_PREDETERMINADO
    api_key_configurada: bool = False


class ProveedorOpenAI:
    nombre = "openai"

    def generar(self, prompt: str, *, instrucciones: str, modelo: str) -> str:
        if not os.getenv("OPENAI_API_KEY"):
            raise NythonIAError(
                "Falta OPENAI_API_KEY. Configura tu clave o usa funciones de Nython sin IA."
            )

        try:
            from openai import OpenAI
        except ImportError as exc:
            raise NythonIAError('Falta instalar el extra de IA. Ejecuta: pip install -e ".[ia]"') from exc

        client = OpenAI()
        respuesta = client.responses.create(
            model=modelo,
            instructions=instrucciones,
            input=prompt,
        )
        return respuesta.output_text


class ProveedorSimulado:
    nombre = "simulado"

    def generar(self, prompt: str, *, instrucciones: str, modelo: str) -> str:
        resumen = " ".join(prompt.split())[:180]
        return (
            "[IA simulada]\n"
            f"Modelo: {modelo}\n"
            "Respuesta: esta es una respuesta local para desarrollo y pruebas.\n"
            f"Prompt recibido: {resumen}"
        )


def leer_configuracion_ia(modelo: str | None = None, proveedor: str | None = None) -> ConfiguracionIA:
    proveedor_final = proveedor or os.getenv("NYTHON_IA_PROVEEDOR", PROVEEDOR_PREDETERMINADO)
    modelo_final = modelo or os.getenv("NYTHON_IA_MODELO", MODELO_PREDETERMINADO)
    return ConfiguracionIA(
        proveedor=proveedor_final,
        modelo=modelo_final,
        api_key_configurada=bool(os.getenv("OPENAI_API_KEY")),
    )


def obtener_proveedor(nombre: str) -> ProveedorIA:
    if nombre == "openai":
        return ProveedorOpenAI()
    if nombre == "simulado":
        return ProveedorSimulado()
    raise NythonIAError(f"Proveedor de IA no soportado: {nombre}")


def ia_disponible(proveedor: str | None = None) -> bool:
    """Indica si el proveedor de IA puede usarse con la configuracion actual."""

    configuracion = leer_configuracion_ia(proveedor=proveedor)
    if configuracion.proveedor == "simulado":
        return True
    if configuracion.proveedor == "openai":
        return configuracion.api_key_configurada
    return False


def estado_ia(proveedor: str | None = None, modelo: str | None = None) -> str:
    configuracion = leer_configuracion_ia(modelo=modelo, proveedor=proveedor)
    disponible = "si" if ia_disponible(configuracion.proveedor) else "no"
    lineas = [
        "Estado de IA en Nython:",
        f"Proveedor: {configuracion.proveedor}",
        f"Modelo: {configuracion.modelo}",
        f"API key configurada: {'si' if configuracion.api_key_configurada else 'no'}",
        f"Disponible: {disponible}",
    ]
    if configuracion.proveedor == "openai" and not configuracion.api_key_configurada:
        lineas.append("Sugerencia: configura OPENAI_API_KEY o usa --proveedor simulado.")
    return "\n".join(lineas)


def preguntar_ia(
    pregunta: str,
    *,
    instrucciones: str = INSTRUCCIONES_BASE,
    modelo: str | None = None,
    proveedor: str | None = None,
) -> str:
    """Pregunta a un proveedor de IA.

    Por defecto usa OpenAI mediante la Responses API. Para desarrollo local puede
    usarse `proveedor="simulado"` sin credenciales ni internet.
    """

    configuracion = leer_configuracion_ia(modelo=modelo, proveedor=proveedor)
    proveedor_ia = obtener_proveedor(configuracion.proveedor)
    return proveedor_ia.generar(
        pregunta,
        instrucciones=instrucciones,
        modelo=configuracion.modelo,
    )


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


def explicar_archivo(
    ruta: str | Path,
    *,
    modelo: str | None = None,
    proveedor: str | None = None,
) -> str:
    codigo_nython = leer_archivo_nython(ruta)
    codigo_python = traducir_codigo(codigo_nython)
    return preguntar_ia(
        crear_prompt_explicacion(codigo_nython, codigo_python),
        modelo=modelo,
        proveedor=proveedor,
    )


def revisar_archivo(
    ruta: str | Path,
    *,
    modelo: str | None = None,
    proveedor: str | None = None,
) -> str:
    codigo_nython = leer_archivo_nython(ruta)
    codigo_python = traducir_codigo(codigo_nython)
    return preguntar_ia(
        crear_prompt_revision(codigo_nython, codigo_python),
        modelo=modelo,
        proveedor=proveedor,
    )
