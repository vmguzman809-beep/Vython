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
```

## Uso desde Ñython

```nython
respuesta = preguntar_ia("Dame un ejemplo de una lista en Python")
imprimir(respuesta)
```

## Diseño

La IA vive en `nython/ia.py` y se conecta como una capa opcional:

- No se importa el SDK de OpenAI hasta que el usuario llama una función de IA.
- Si falta `OPENAI_API_KEY`, Ñython muestra un error claro.
- Si falta el extra `ia`, Ñython explica cómo instalarlo.
- La CLI puede explicar o revisar archivos traduciendo primero el código Ñython a Python.
