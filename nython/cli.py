"""Interfaz de linea de comandos de Nython."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import __version__
from .ejecutor import ejecutar_archivo, traducir_archivo
from .errores import formatear_error
from .utilidades import escribir_archivo_python


def crear_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="nython",
        description="Programa en espanol. Ejecuta en Python.",
    )
    subparsers = parser.add_subparsers(dest="comando")

    ejecutar = subparsers.add_parser("ejecutar", help="Ejecuta un archivo .ny o .nython")
    ejecutar.add_argument("archivo")

    traducir = subparsers.add_parser("traducir", help="Imprime el codigo Python generado")
    traducir.add_argument("archivo")

    compilar = subparsers.add_parser("compilar", help="Guarda el codigo Python generado")
    compilar.add_argument("archivo")
    compilar.add_argument("-o", "--salida", required=True)

    subparsers.add_parser("version", help="Muestra la version instalada")
    subparsers.add_parser("ayuda", help="Muestra esta ayuda")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = crear_parser()
    args = parser.parse_args(argv)

    if args.comando in {None, "ayuda"}:
        parser.print_help()
        return 0

    try:
        if args.comando == "version":
            print(f"Nython {__version__}")
            return 0

        if args.comando == "ejecutar":
            ejecutar_archivo(args.archivo)
            return 0

        if args.comando == "traducir":
            print(traducir_archivo(args.archivo), end="")
            return 0

        if args.comando == "compilar":
            codigo_python = traducir_archivo(args.archivo)
            salida = escribir_archivo_python(Path(args.salida), codigo_python)
            print(f"Archivo Python generado: {salida}")
            return 0
    except Exception as error:  # noqa: BLE001 - CLI debe presentar cualquier error al usuario.
        print(formatear_error(error, getattr(args, "archivo", None)), file=sys.stderr)
        return 1

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
