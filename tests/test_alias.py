from nython.alias import crear_entorno_alias


def test_alias_basicos_existen() -> None:
    alias = crear_entorno_alias()

    assert alias["imprimir"] is print
    assert alias["entrada"] is input
    assert alias["rango"] is range
    assert alias["longitud"] is len
