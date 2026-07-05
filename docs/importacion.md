# Importación de módulos `.ny`

Ñython incluye un importador inicial para cargar módulos escritos en `.ny` o `.nython`.

Archivo `matematicas.ny`:

```nython
funcion multiplicar(a, b):
    retornar a * b
```

Archivo `programa.ny`:

```nython
desde matematicas importar multiplicar

resultado = multiplicar(5, 7)
imprimir(resultado)
```

Al ejecutar `programa.ny`, el importador encuentra `matematicas.ny`, lo traduce a Python y carga el módulo de forma transparente.

```bash
nython ejecutar ejemplos/importar_modulo.ny
```
