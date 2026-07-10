# Ñython para VS Code

Extensión base para trabajar con archivos `.ny` y `.nython`.

## Funciones

- Reconocimiento de archivos `.ny` y `.nython`.
- Resaltado de sintaxis básico.
- Snippets para `si`, `para`, `funcion` y `repetir`.
- Comandos:
  - `Ñython: Ejecutar archivo actual`
  - `Ñython: Traducir archivo actual`
  - `Ñython: Compilar archivo actual`

## Requisito

Instala Ñython en tu entorno:

```bash
pip install -e .
```

## Empaquetar

Desde `vscode-extension/`:

```bash
npm install -g @vscode/vsce
vsce package
```
