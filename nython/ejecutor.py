"""Ejecucion de archivos Nython."""

from __future__ import annotations

import sys
from pathlib import Path
from types import SimpleNamespace

from .alias import crear_entorno_alias
from .importador import instalar_importador
from .traductor import traducir_codigo
from .utilidades import leer_archivo_nython


def traducir_archivo(ruta: str | Path) -> str:
    codigo = leer_archivo_nython(ruta)
    return traducir_codigo(codigo)


def ejecutar_archivo(ruta: str | Path) -> SimpleNamespace:
    path = Path(ruta)
    instalar_importador()
    agregar_directorio_a_sys_path(path.parent)
    codigo_python = traducir_archivo(path)
    entorno = crear_entorno(path)
    compilado = compile(codigo_python, str(path), "exec")
    exec(compilado, entorno)
    return SimpleNamespace(codigo_python=codigo_python, entorno=entorno)


def crear_entorno(path: Path) -> dict[str, object]:
    entorno: dict[str, object] = {
        "__name__": "__main__",
        "__file__": str(path),
        "__package__": None,
    }
    entorno.update(crear_entorno_alias())
    return entorno


def agregar_directorio_a_sys_path(path: Path) -> None:
    directorio = str(path.resolve())
    if directorio not in sys.path:
        sys.path.insert(0, directorio)
