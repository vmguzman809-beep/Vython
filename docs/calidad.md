# Calidad del proyecto

Ñython usa pruebas automatizadas, lint y cobertura básica para cuidar la base del proyecto.

## Instalar herramientas de desarrollo

```bash
pip install -e ".[dev]"
```

## Ejecutar pruebas

```bash
pytest
```

## Ejecutar lint

```bash
ruff check .
```

## Ejecutar cobertura

```bash
coverage run -m pytest
coverage report
```

## Verificar paquete

```bash
python -m build
python -m twine check dist/*
```

## Sitio de documentación

```bash
mkdocs build
mkdocs serve
```

## CI

GitHub Actions ejecuta lint, pruebas y cobertura en Python 3.10, 3.11 y 3.12.
