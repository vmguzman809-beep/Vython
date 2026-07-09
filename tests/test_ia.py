import pytest

from nython.ia import (
    NythonIAError,
    convertir_python,
    crear_prompt_conversion_python,
    crear_prompt_ejercicio,
    crear_prompt_error,
    crear_prompt_explicacion,
    crear_prompt_revision,
    estado_ia,
    generar_ejercicio,
    ia_disponible,
    leer_configuracion_ia,
    obtener_proveedor,
    preguntar_ia,
)


def test_ia_disponible_depende_de_api_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    assert ia_disponible() is False
    assert ia_disponible("simulado") is True

    monkeypatch.setenv("OPENAI_API_KEY", "test")
    assert ia_disponible() is True


def test_preguntar_ia_falla_sin_api_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)

    with pytest.raises(NythonIAError, match="OPENAI_API_KEY"):
        preguntar_ia("Hola")


def test_preguntar_ia_simulada_no_requiere_api_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)

    respuesta = preguntar_ia("Hola", proveedor="simulado", modelo="prueba")

    assert "[IA simulada]" in respuesta
    assert "Modelo: prueba" in respuesta


def test_estado_ia_muestra_configuracion(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)

    estado = estado_ia(proveedor="openai", modelo="modelo-test")

    assert "Proveedor: openai" in estado
    assert "Modelo: modelo-test" in estado
    assert "API key configurada: no" in estado


def test_configuracion_lee_variables_de_entorno(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("NYTHON_IA_PROVEEDOR", "simulado")
    monkeypatch.setenv("NYTHON_IA_MODELO", "modelo-env")

    configuracion = leer_configuracion_ia()

    assert configuracion.proveedor == "simulado"
    assert configuracion.modelo == "modelo-env"


def test_proveedor_desconocido_falla() -> None:
    with pytest.raises(NythonIAError, match="Proveedor"):
        obtener_proveedor("otro")


def test_prompt_explicacion_incluye_codigo_nython_y_python() -> None:
    prompt = crear_prompt_explicacion('imprimir("hola")', 'print("hola")')

    assert "Codigo Nython" in prompt
    assert 'imprimir("hola")' in prompt
    assert 'print("hola")' in prompt


def test_prompt_revision_incluye_contexto_de_tutor() -> None:
    prompt = crear_prompt_revision('imprimir("hola")', 'print("hola")')

    assert "tutor" in prompt
    assert "Python generado" in prompt


def test_prompt_error_incluye_codigo_y_error() -> None:
    prompt = crear_prompt_error('imprimir(valor)', "print(valor)", "Nombre no definido")

    assert "Explica este error" in prompt
    assert "Nombre no definido" in prompt


def test_generar_ejercicio_usa_proveedor_simulado() -> None:
    respuesta = generar_ejercicio("listas", proveedor="simulado")

    assert "[IA simulada]" in respuesta
    assert "listas" in respuesta


def test_convertir_python_usa_archivo(tmp_path) -> None:
    archivo = tmp_path / "programa.py"
    archivo.write_text('print("hola")\n', encoding="utf-8")

    respuesta = convertir_python(archivo, proveedor="simulado")

    assert "[IA simulada]" in respuesta
    assert "print" in respuesta


def test_prompts_nuevos_son_educativos() -> None:
    assert "ejercicio educativo" in crear_prompt_ejercicio("bucles")
    assert "Convierte este codigo Python" in crear_prompt_conversion_python("print('hola')")
