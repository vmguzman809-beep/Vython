"""Importador para cargar modulos escritos en archivos .ny o .nython."""

from __future__ import annotations

import importlib.abc
import importlib.machinery
import sys
from pathlib import Path

from .traductor import traducir_codigo

EXTENSIONES_NYTHON = (".ny", ".nython")


class NythonLoader(importlib.abc.SourceLoader):
    def __init__(self, fullname: str, path: Path, es_paquete: bool = False) -> None:
        self.fullname = fullname
        self.path = path
        self.es_paquete = es_paquete

    def get_filename(self, fullname: str) -> str:
        return str(self.path)

    def get_data(self, path: str) -> bytes:
        return Path(path).read_bytes()

    def is_package(self, fullname: str) -> bool:
        return self.es_paquete

    def source_to_code(self, data: bytes, path: str, *, _optimize: int = -1):
        codigo_nython = data.decode("utf-8")
        codigo_python = traducir_codigo(codigo_nython)
        return compile(codigo_python, path, "exec", dont_inherit=True, optimize=_optimize)


class NythonFinder(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname: str, path: list[str] | None, target=None):
        nombre_modulo = fullname.rsplit(".", 1)[-1]
        rutas = path or sys.path

        for entrada in rutas:
            if not entrada:
                entrada = "."
            base = Path(entrada)
            for extension in EXTENSIONES_NYTHON:
                candidato = base / f"{nombre_modulo}{extension}"
                if candidato.is_file():
                    loader = NythonLoader(fullname, candidato)
                    return importlib.machinery.ModuleSpec(fullname, loader, origin=str(candidato))

                paquete = base / nombre_modulo / f"__init__{extension}"
                if paquete.is_file():
                    loader = NythonLoader(fullname, paquete, es_paquete=True)
                    spec = importlib.machinery.ModuleSpec(
                        fullname,
                        loader,
                        origin=str(paquete),
                        is_package=True,
                    )
                    spec.submodule_search_locations = [str(paquete.parent)]
                    return spec

        return None


def instalar_importador() -> None:
    if not any(isinstance(finder, NythonFinder) for finder in sys.meta_path):
        sys.meta_path.insert(0, NythonFinder())
