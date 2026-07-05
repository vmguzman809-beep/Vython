import pytest

from nython.ia import (
    NythonIAError,
    crear_prompt_explicacion,
    crear_prompt_revision,
    ia_disponible,
    preguntar_ia,
)


def test_ia_disponible_depende_de_api_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    assert ia_disponible() is False

    monkeypatch.setenv("OPENAI_API_KEY", "test")
    assert ia_disponible() is True


def test_preguntar_ia_falla_sin_api_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)

    with pytest.raises(NythonIAError, match="OPENAI_API_KEY"):
        preguntar_ia("Hola")


def test_prompt_explicacion_incluye_codigo_nython_y_python() -> None:
    prompt = crear_prompt_explicacion('imprimir("hola")', 'print("hola")')

    assert "Codigo Nython" in prompt
    assert 'imprimir("hola")' in prompt
    assert 'print("hola")' in prompt


def test_prompt_revision_incluye_contexto_de_tutor() -> None:
    prompt = crear_prompt_revision('imprimir("hola")', 'print("hola")')

    assert "tutor" in prompt
    assert "Python generado" in prompt
