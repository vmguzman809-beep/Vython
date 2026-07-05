# Sintaxis

Ñython traduce palabras clave y alias comunes usando el analizador de tokens de Python. Esto evita reemplazos dentro de strings y comentarios.

```nython
imprimir("si sino para")
```

Se traduce a:

```python
print("si sino para")
```

Los identificadores pueden usar caracteres Unicode aceptados por Python, incluyendo `ñ` y vocales acentuadas.
