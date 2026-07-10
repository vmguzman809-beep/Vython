# Changelog

## 0.2.0

- Agrega arquitectura IA con proveedores `openai` y `simulado`.
- Agrega comandos IA: `estado`, `explicar-error`, `generar-ejercicio` y `convertir-python`.
- Hace que `explicar-error` compile sin ejecutar por defecto, con `--ejecutar` para errores runtime.
- Protege strings multilínea al aplicar reglas de gramática natural.
- Mejora errores con contexto de código.
- Agrega importación de paquetes Ñython mediante `__init__.ny`.
- Agrega lint, cobertura y metadata del paquete.
- Agrega configuración MkDocs y workflow de release para construir paquetes.
- Mejora la extensión VS Code con comandos para ejecutar, traducir y compilar.
- Agrega snippets básicos para VS Code.

## 0.1.0

- MVP inicial de Ñython.
- Transpilador `.ny` y `.nython` a Python.
- CLI básica.
- Alias en español.
- Errores amigables.
- Ejemplos, documentación y pruebas.
