from nython.traductor import traducir_codigo


def normalizar(codigo: str) -> str:
    return codigo.strip()


def test_traduce_para_cada() -> None:
    codigo = """para cada persona en personas:
    imprimir(persona)
"""

    assert normalizar(traducir_codigo(codigo)) == "for persona in personas:\n    print(persona)"


def test_traduce_repetir_veces() -> None:
    codigo = """repetir 3 veces:
    imprimir("Hola")
"""

    assert normalizar(traducir_codigo(codigo)) == 'for _ in range(3):\n    print("Hola")'


def test_traduce_esta_entre() -> None:
    codigo = """si edad esta entre 18 y 65:
    imprimir("ok")
"""

    assert normalizar(traducir_codigo(codigo)) == 'if 18 <= edad <= 65:\n    print("ok")'


def test_traduce_condicional_y_alias() -> None:
    codigo = """si verdadero:
    imprimir("ok")
"""

    assert normalizar(traducir_codigo(codigo)) == 'if True:\n    print("ok")'


def test_no_modifica_strings() -> None:
    codigo = 'imprimir("si sino para")'

    assert normalizar(traducir_codigo(codigo)) == 'print("si sino para")'


def test_traduce_bucle_para_en_rango() -> None:
    codigo = """para numero en rango(1, 3):
    imprimir(numero)
"""

    assert normalizar(traducir_codigo(codigo)) == "for numero in range(1, 3):\n    print(numero)"


def test_soporta_identificadores_con_acentos() -> None:
    codigo = """año = 2026
si año > 2020:
    imprimir(año)
"""

    assert "año" in traducir_codigo(codigo)
