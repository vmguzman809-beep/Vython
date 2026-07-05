"""Alias basicos en espanol para funciones comunes de Python."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any


ALIAS_FUNCIONES: dict[str, Callable[..., Any] | type] = {
    "imprimir": print,
    "entrada": input,
    "rango": range,
    "longitud": len,
    "entero": int,
    "decimal": float,
    "texto": str,
    "booleano": bool,
    "lista": list,
    "tupla": tuple,
    "conjunto": set,
    "diccionario": dict,
    "enumerar": enumerate,
    "zippear": zip,
    "sumar": sum,
    "maximo": max,
    "minimo": min,
    "absoluto": abs,
    "redondear": round,
    "ordenado": sorted,
    "tipo": type,
    "abrir": open,
}


def crear_entorno_alias() -> dict[str, Callable[..., Any] | type]:
    """Devuelve una copia del entorno de alias para ejecutar codigo Nython."""

    return dict(ALIAS_FUNCIONES)
