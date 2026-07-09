"""Transpilador de codigo Nython a Python."""

from __future__ import annotations

import io
import re
import tokenize
from token import NAME, STRING

from .alias import ALIAS_FUNCIONES

PALABRAS_CLAVE: dict[str, str] = {
    "si": "if",
    "sino": "else",
    "osi": "elif",
    "para": "for",
    "mientras": "while",
    "en": "in",
    "definir": "def",
    "funcion": "def",
    "retornar": "return",
    "verdadero": "True",
    "falso": "False",
    "nulo": "None",
    "y": "and",
    "o": "or",
    "no": "not",
    "clase": "class",
    "importar": "import",
    "desde": "from",
    "como": "as",
    "intentar": "try",
    "excepto": "except",
    "finalmente": "finally",
    "con": "with",
    "romper": "break",
    "continuar": "continue",
    "pasar": "pass",
    "global": "global",
    "no_local": "nonlocal",
    "afirmar": "assert",
    "eliminar": "del",
    "lanzar": "raise",
    "ceder": "yield",
    "esperar": "await",
    "asincrono": "async",
    "lambda": "lambda",
}


ALIAS_TRADUCIBLES: dict[str, str] = {
    "imprimir": "print",
    "entrada": "input",
    "rango": "range",
    "longitud": "len",
    "entero": "int",
    "decimal": "float",
    "texto": "str",
    "booleano": "bool",
    "lista": "list",
    "tupla": "tuple",
    "conjunto": "set",
    "diccionario": "dict",
    "enumerar": "enumerate",
    "zippear": "zip",
    "sumar": "sum",
    "maximo": "max",
    "minimo": "min",
    "absoluto": "abs",
    "redondear": "round",
    "ordenado": "sorted",
    "tipo": "type",
    "abrir": "open",
}

TRADUCCIONES = PALABRAS_CLAVE | ALIAS_TRADUCIBLES


PATRON_PARA_CADA = re.compile(r"^(?P<indent>\s*)para\s+cada\s+(?P<var>\w+)\s+en\s+(?P<iterable>.+):\s*$")
PATRON_REPETIR = re.compile(r"^(?P<indent>\s*)repetir\s+(?P<veces>.+?)\s+veces:\s*$")
PATRON_ESTA_ENTRE = re.compile(
    r"^(?P<indent>\s*)si\s+(?P<valor>.+?)\s+esta\s+entre\s+(?P<minimo>.+?)\s+y\s+(?P<maximo>.+?):\s*$"
)


def traducir_codigo(codigo: str) -> str:
    """Traduce codigo Nython a Python preservando strings y comentarios."""

    codigo = aplicar_reglas_naturales(codigo)
    tokens = tokenize.generate_tokens(io.StringIO(codigo).readline)
    traducidos: list[tokenize.TokenInfo] = []

    for token in tokens:
        if token.type == NAME and token.string in TRADUCCIONES:
            token = token._replace(string=TRADUCCIONES[token.string])
        traducidos.append(token)

    return tokenize.untokenize(traducidos)


def aplicar_reglas_naturales(codigo: str) -> str:
    """Aplica reglas de sintaxis natural antes de traducir tokens.

    Las reglas se aplican por linea, pero se saltan lineas cubiertas por strings
    multilínea para no modificar texto educativo o plantillas dentro de comillas.
    """

    lineas_protegidas = _lineas_en_strings_multilinea(codigo)
    traducidas: list[str] = []
    for numero, linea in enumerate(codigo.splitlines(keepends=True), start=1):
        if numero in lineas_protegidas:
            traducidas.append(linea)
        else:
            traducidas.append(_traducir_linea_natural(linea))
    return "".join(traducidas)


def _traducir_linea_natural(linea: str) -> str:
    salto = ""
    cuerpo = linea
    if linea.endswith("\r\n"):
        cuerpo, salto = linea[:-2], "\r\n"
    elif linea.endswith("\n"):
        cuerpo, salto = linea[:-1], "\n"

    if coincidencia := PATRON_PARA_CADA.match(cuerpo):
        grupos = coincidencia.groupdict()
        return f"{grupos['indent']}para {grupos['var']} en {grupos['iterable']}:{salto}"

    if coincidencia := PATRON_REPETIR.match(cuerpo):
        grupos = coincidencia.groupdict()
        return f"{grupos['indent']}para _ en rango({grupos['veces']}):{salto}"

    if coincidencia := PATRON_ESTA_ENTRE.match(cuerpo):
        grupos = coincidencia.groupdict()
        return f"{grupos['indent']}si {grupos['minimo']} <= {grupos['valor']} <= {grupos['maximo']}:{salto}"

    return linea


def _lineas_en_strings_multilinea(codigo: str) -> set[int]:
    protegidas: set[int] = set()
    try:
        tokens = tokenize.generate_tokens(io.StringIO(codigo).readline)
        for token in tokens:
            if token.type == STRING and token.start[0] != token.end[0]:
                protegidas.update(range(token.start[0], token.end[0] + 1))
    except tokenize.TokenError:
        return protegidas
    return protegidas


def obtener_tabla_traducciones() -> dict[str, str]:
    """Devuelve las equivalencias principales del lenguaje."""

    return dict(TRADUCCIONES)


def obtener_alias_ejecucion() -> dict[str, object]:
    """Expone los alias disponibles al ejecutar codigo traducido."""

    return dict(ALIAS_FUNCIONES)
