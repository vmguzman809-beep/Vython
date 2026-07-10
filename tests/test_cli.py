from pathlib import Path

from nython.cli import main


def test_cli_version(capsys) -> None:
    assert main(["version"]) == 0

    assert "Nython" in capsys.readouterr().out


def test_cli_ayuda(capsys) -> None:
    assert main(["ayuda"]) == 0

    assert "Programa en espanol" in capsys.readouterr().out


def test_cli_traducir(tmp_path: Path, capsys) -> None:
    archivo = tmp_path / "programa.ny"
    archivo.write_text('imprimir("hola")\n', encoding="utf-8")

    assert main(["traducir", str(archivo)]) == 0

    assert 'print("hola")' in capsys.readouterr().out


def test_cli_compilar(tmp_path: Path, capsys) -> None:
    archivo = tmp_path / "programa.ny"
    salida = tmp_path / "programa.py"
    archivo.write_text('imprimir("hola")\n', encoding="utf-8")

    assert main(["compilar", str(archivo), "-o", str(salida)]) == 0

    assert salida.read_text(encoding="utf-8").strip() == 'print("hola")'
    assert "Archivo Python generado" in capsys.readouterr().out


def test_cli_ejecutar(tmp_path: Path, capsys) -> None:
    archivo = tmp_path / "programa.ny"
    archivo.write_text('imprimir("hola")\n', encoding="utf-8")

    assert main(["ejecutar", str(archivo)]) == 0

    assert capsys.readouterr().out.strip() == "hola"


def test_cli_ia_estado_simulado(capsys) -> None:
    assert main(["ia", "estado", "--proveedor", "simulado"]) == 0

    assert "Proveedor: simulado" in capsys.readouterr().out


def test_cli_ia_generar_ejercicio_simulado(capsys) -> None:
    assert main(["ia", "generar-ejercicio", "listas", "--proveedor", "simulado"]) == 0

    assert "[IA simulada]" in capsys.readouterr().out


def test_cli_error_amigable(tmp_path: Path, capsys) -> None:
    archivo = tmp_path / "programa.txt"
    archivo.write_text("nada", encoding="utf-8")

    assert main(["traducir", str(archivo)]) == 1

    assert "Error en Nython" in capsys.readouterr().err
