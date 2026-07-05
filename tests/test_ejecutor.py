from pathlib import Path

from nython.ejecutor import ejecutar_archivo, traducir_archivo


def test_traducir_archivo_temporal(tmp_path: Path) -> None:
    archivo = tmp_path / "programa.ny"
    archivo.write_text('imprimir("hola")', encoding="utf-8")

    assert traducir_archivo(archivo).strip() == 'print("hola")'


def test_ejecutar_archivo_temporal(tmp_path: Path, capsys) -> None:
    archivo = tmp_path / "programa.ny"
    archivo.write_text('imprimir("hola")', encoding="utf-8")

    ejecutar_archivo(archivo)

    assert capsys.readouterr().out.strip() == "hola"


def test_importa_modulo_nython(tmp_path: Path, capsys) -> None:
    modulo = tmp_path / "matematicas.ny"
    programa = tmp_path / "programa.ny"
    modulo.write_text("funcion duplicar(valor):\n    retornar valor * 2\n", encoding="utf-8")
    programa.write_text("desde matematicas importar duplicar\nimprimir(duplicar(4))\n", encoding="utf-8")

    ejecutar_archivo(programa)

    assert capsys.readouterr().out.strip() == "8"
