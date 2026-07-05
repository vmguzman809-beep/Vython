from nython.errores import formatear_error, sugerencia_para


def test_sugerencia_para_name_error() -> None:
    mensaje = sugerencia_para(NameError("name 'x' is not defined"))

    assert "falta definirlo" in mensaje


def test_formatea_error_en_espanol() -> None:
    mensaje = formatear_error(ValueError("dato invalido"), "programa.ny")

    assert "Error en Nython:" in mensaje
    assert "Tipo: Valor invalido" in mensaje
    assert "Archivo: programa.ny" in mensaje


def test_indentation_error_usa_nombre_especifico() -> None:
    mensaje = formatear_error(IndentationError("indentacion"), "programa.ny")

    assert "Tipo: Error de indentacion" in mensaje


def test_error_ia_no_muestra_linea_interna() -> None:
    class NythonIAError(RuntimeError):
        pass

    mensaje = formatear_error(NythonIAError("falta clave"))

    assert "Tipo: Error de IA" in mensaje
    assert "Archivo: configuracion de IA" in mensaje
    assert "Linea: desconocida" in mensaje
