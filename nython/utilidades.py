"""Utilidades compartidas del proyecto Nython."""

from __future__ import annotations

from pathlib import Path

EXTENSIONES_VALIDAS = {".ny", ".nython"}


def validar_extension(ruta: str | Path) -> Path:
    path = Path(ruta)
    if path.suffix not in EXTENSIONES_VALIDAS:
        extensiones = ", ".join(sorted(EXTENSIONES_VALIDAS))
        raise ValueError(f"Extension no soportada: {path.suffix}. Usa {extensiones}.")
    return path


def leer_archivo_nython(ruta: str | Path) -> str:
    path = validar_extension(ruta)
    return path.read_text(encoding="utf-8")


def escribir_archivo_python(ruta: str | Path, codigo: str) -> Path:
    path = Path(ruta)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(codigo, encoding="utf-8")
    return path
