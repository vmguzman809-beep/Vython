# IA nativa opcional

Ñython puede usar IA como tutor integrado, pero el lenguaje no depende de ella. El transpilador, la CLI básica, los ejemplos y las pruebas funcionan sin internet ni credenciales.

## Instalación

```bash
pip install -e ".[ia]"
```

## Configuración

Define la variable `OPENAI_API_KEY`.

PowerShell:

```powershell
setx OPENAI_API_KEY "tu_clave"
```

Linux o macOS:

```bash
export OPENAI_API_KEY="tu_clave"
```

Opcionalmente puedes cambiar el modelo:

```bash
setx NYTHON_IA_MODELO "gpt-5.5"
```

## Uso desde la CLI

```bash
nython ia preguntar "Explícame qué es una variable"
nython ia explicar ejemplos/condicionales.ny
nython ia revisar ejemplos/funciones.ny
nython ia explicar-error ejemplos/error_nombre.ny
nython ia generar-ejercicio listas --nivel principiante
nython ia convertir-python programa.py
nython ia estado
```

## Modo simulado

Para desarrollo, demos o pruebas sin credenciales puedes usar el proveedor simulado:

```bash
nython ia estado --proveedor simulado
nython ia preguntar "Explícame una lista" --proveedor simulado
nython ia explicar ejemplos/hola_mundo.ny --proveedor simulado
```

También puede configurarse por entorno:

```bash
setx NYTHON_IA_PROVEEDOR "simulado"
```

## Uso desde Ñython

```nython
respuesta = preguntar_ia("Dame un ejemplo de una lista en Python")
imprimir(respuesta)
```

Para usar el modo simulado desde un archivo:

```nython
respuesta = preguntar_ia("Dame una idea de ejercicio con listas", proveedor="simulado")
imprimir(respuesta)
```

## Diseño

La IA vive en `nython/ia.py` y se conecta como una capa opcional:

- No se importa el SDK de OpenAI hasta que el usuario llama una función de IA.
- Si falta `OPENAI_API_KEY`, Ñython muestra un error claro.
- Si falta el extra `ia`, Ñython explica cómo instalarlo.
- La CLI puede explicar o revisar archivos traduciendo primero el código Ñython a Python.
- El proveedor `simulado` permite probar la experiencia sin internet, API key ni costo.
