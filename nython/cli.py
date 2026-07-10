"""Interfaz de linea de comandos de Nython."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import __version__
from .ejecutor import ejecutar_archivo, traducir_archivo
from .errores import formatear_error
from .ia import (
    convertir_python,
    estado_ia,
    explicar_archivo,
    explicar_error_archivo,
    generar_ejercicio,
    preguntar_ia,
    revisar_archivo,
)
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

    ia = subparsers.add_parser("ia", help="Herramientas opcionales con inteligencia artificial")
    ia_subparsers = ia.add_subparsers(dest="accion_ia")

    ia_preguntar = ia_subparsers.add_parser("preguntar", help="Pregunta libre al asistente IA")
    ia_preguntar.add_argument("pregunta")
    ia_preguntar.add_argument("--modelo")
    ia_preguntar.add_argument("--proveedor", choices=["openai", "simulado"])

    ia_explicar = ia_subparsers.add_parser("explicar", help="Explica un archivo Nython")
    ia_explicar.add_argument("archivo")
    ia_explicar.add_argument("--modelo")
    ia_explicar.add_argument("--proveedor", choices=["openai", "simulado"])

    ia_revisar = ia_subparsers.add_parser("revisar", help="Revisa un archivo Nython")
    ia_revisar.add_argument("archivo")
    ia_revisar.add_argument("--modelo")
    ia_revisar.add_argument("--proveedor", choices=["openai", "simulado"])

    ia_error = ia_subparsers.add_parser("explicar-error", help="Explica el error de un archivo Nython")
    ia_error.add_argument("archivo")
    ia_error.add_argument("--modelo")
    ia_error.add_argument("--proveedor", choices=["openai", "simulado"])
    ia_error.add_argument(
        "--ejecutar",
        action="store_true",
        help="Ejecuta el archivo para capturar errores en tiempo de ejecucion.",
    )

    ia_ejercicio = ia_subparsers.add_parser("generar-ejercicio", help="Genera un ejercicio educativo")
    ia_ejercicio.add_argument("tema")
    ia_ejercicio.add_argument("--nivel", default="principiante")
    ia_ejercicio.add_argument("--modelo")
    ia_ejercicio.add_argument("--proveedor", choices=["openai", "simulado"])

    ia_convertir = ia_subparsers.add_parser("convertir-python", help="Convierte un archivo Python a Nython")
    ia_convertir.add_argument("archivo")
    ia_convertir.add_argument("--modelo")
    ia_convertir.add_argument("--proveedor", choices=["openai", "simulado"])

    ia_estado = ia_subparsers.add_parser("estado", help="Muestra la configuracion de IA")
    ia_estado.add_argument("--modelo")
    ia_estado.add_argument("--proveedor", choices=["openai", "simulado"])

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

        if args.comando == "ia":
            if args.accion_ia == "preguntar":
                print(preguntar_ia(args.pregunta, modelo=args.modelo, proveedor=args.proveedor))
                return 0
            if args.accion_ia == "explicar":
                print(explicar_archivo(args.archivo, modelo=args.modelo, proveedor=args.proveedor))
                return 0
            if args.accion_ia == "revisar":
                print(revisar_archivo(args.archivo, modelo=args.modelo, proveedor=args.proveedor))
                return 0
            if args.accion_ia == "explicar-error":
                print(
                    explicar_error_archivo(
                        args.archivo,
                        modelo=args.modelo,
                        proveedor=args.proveedor,
                        ejecutar=args.ejecutar,
                    )
                )
                return 0
            if args.accion_ia == "generar-ejercicio":
                print(
                    generar_ejercicio(
                        args.tema,
                        nivel=args.nivel,
                        modelo=args.modelo,
                        proveedor=args.proveedor,
                    )
                )
                return 0
            if args.accion_ia == "convertir-python":
                print(convertir_python(args.archivo, modelo=args.modelo, proveedor=args.proveedor))
                return 0
            if args.accion_ia == "estado":
                print(estado_ia(modelo=args.modelo, proveedor=args.proveedor))
                return 0
            parser.parse_args(["ia", "--help"])
            return 0
    except Exception as error:  # noqa: BLE001 - CLI debe presentar cualquier error al usuario.
        print(formatear_error(error, getattr(args, "archivo", None)), file=sys.stderr)
        return 1

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
