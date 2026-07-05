"""Transpilador de codigo Nython a Python."""

from __future__ import annotations

import io
import re
import tokenize
from token import NAME

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
    """Aplica reglas de sintaxis natural antes de traducir tokens."""

    return "\n".join(_traducir_linea_natural(linea) for linea in codigo.splitlines())


def _traducir_linea_natural(linea: str) -> str:
    if coincidencia := PATRON_PARA_CADA.match(linea):
        grupos = coincidencia.groupdict()
        return f"{grupos['indent']}para {grupos['var']} en {grupos['iterable']}:"

    if coincidencia := PATRON_REPETIR.match(linea):
        grupos = coincidencia.groupdict()
        return f"{grupos['indent']}para _ en rango({grupos['veces']}):"

    if coincidencia := PATRON_ESTA_ENTRE.match(linea):
        grupos = coincidencia.groupdict()
        return f"{grupos['indent']}si {grupos['minimo']} <= {grupos['valor']} <= {grupos['maximo']}:"

    return linea


def obtener_tabla_traducciones() -> dict[str, str]:
    """Devuelve las equivalencias principales del lenguaje."""

    return dict(TRADUCCIONES)


def obtener_alias_ejecucion() -> dict[str, object]:
    """Expone los alias disponibles al ejecutar codigo traducido."""

    return dict(ALIAS_FUNCIONES)
