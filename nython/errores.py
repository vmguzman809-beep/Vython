"""Formato de errores amigables para usuarios de Nython."""

from __future__ import annotations

import traceback
from pathlib import Path


TIPOS_ERROR: dict[type[BaseException], str] = {
    IndentationError: "Error de indentacion",
    ModuleNotFoundError: "Modulo no encontrado",
    SyntaxError: "Error de sintaxis",
    NameError: "Nombre no definido",
    TypeError: "Error de tipo",
    ValueError: "Valor invalido",
    IndexError: "Indice fuera de rango",
    KeyError: "Clave no encontrada",
    ZeroDivisionError: "Division entre cero",
    FileNotFoundError: "Archivo no encontrado",
    ImportError: "Error al importar modulo",
    AttributeError: "Atributo no encontrado",
}


def nombre_error(error: BaseException) -> str:
    if error.__class__.__name__ == "NythonIAError":
        return "Error de IA"
    for tipo, nombre in TIPOS_ERROR.items():
        if isinstance(error, tipo):
            return nombre
    return error.__class__.__name__


def obtener_linea_error(error: BaseException) -> int | None:
    if error.__class__.__name__ == "NythonIAError":
        return None
    if isinstance(error, SyntaxError):
        return error.lineno

    tb = error.__traceback__
    ultimo = None
    while tb:
        ultimo = tb
        tb = tb.tb_next
    return ultimo.tb_lineno if ultimo else None


def sugerencia_para(error: BaseException) -> str:
    if error.__class__.__name__ == "NythonIAError":
        return 'Instala el extra con `pip install -e ".[ia]"` y configura OPENAI_API_KEY.'
    if isinstance(error, IndentationError):
        return "Revisa los espacios al inicio de la linea. Los bloques deben mantener la misma indentacion."
    if isinstance(error, ModuleNotFoundError):
        return "Revisa si el modulo existe, si esta instalado o si el archivo .ny esta en la misma carpeta."
    if isinstance(error, SyntaxError):
        detalle = str(error).lower()
        if "expected ':'" in detalle or "invalid syntax" in detalle:
            return 'Revisa si falta ":" al final de la linea o si hay una palabra mal escrita.'
        return "Revisa la sintaxis, los parentesis, las comillas y la indentacion."
    if isinstance(error, NameError):
        return "Revisa si el nombre esta escrito correctamente o si falta definirlo antes."
    if isinstance(error, TypeError):
        return "Revisa los tipos de datos que estas combinando o pasando a la funcion."
    if isinstance(error, ValueError):
        return "Revisa que el valor tenga el formato esperado."
    if isinstance(error, FileNotFoundError):
        return "Revisa la ruta del archivo y que exista en tu proyecto."
    return "Lee el detalle del error y revisa la linea indicada."


def formatear_error(error: BaseException, archivo: str | Path | None = None) -> str:
    archivo_texto = str(archivo) if archivo else obtener_archivo_error(error)
    linea = obtener_linea_error(error)
    linea_texto = str(linea) if linea is not None else "desconocida"

    return "\n".join(
        [
            "Error en Nython:",
            f"Tipo: {nombre_error(error)}",
            f"Archivo: {archivo_texto}",
            f"Linea: {linea_texto}",
            f"Detalle: {error}",
            f"Sugerencia: {sugerencia_para(error)}",
        ]
    )


def obtener_archivo_error(error: BaseException) -> str:
    if error.__class__.__name__ == "NythonIAError":
        return "configuracion de IA"
    if isinstance(error, SyntaxError) and error.filename:
        return error.filename

    tb = traceback.extract_tb(error.__traceback__) if error.__traceback__ else []
    return tb[-1].filename if tb else "desconocido"
