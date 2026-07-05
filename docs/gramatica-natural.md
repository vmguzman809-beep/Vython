# Gramática natural

Ñython ya incluye reglas iniciales para escribir algunas estructuras de forma más cercana al español.

## `para cada`

```nython
para cada persona en personas:
    imprimir(persona)
```

Python generado:

```python
for persona in personas:
    print(persona)
```

## `repetir N veces`

```nython
repetir 3 veces:
    imprimir("Hola")
```

Python generado:

```python
for _ in range(3):
    print("Hola")
```

## `esta entre`

```nython
si edad esta entre 18 y 65:
    imprimir("Edad laboral")
```

Python generado:

```python
if 18 <= edad <= 65:
    print("Edad laboral")
```
