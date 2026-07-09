# Ñython

[![Tests](https://github.com/vmguzman809-beep/Vython/actions/workflows/tests.yml/badge.svg)](https://github.com/vmguzman809-beep/Vython/actions/workflows/tests.yml)

**Programa en español. Ejecuta en Python.**

Ñython es una herramienta educativa para escribir código con sintaxis en español y ejecutarlo como Python real. No busca reemplazar Python. Busca acercar Python a millones de hispanohablantes que están aprendiendo a programar.

## Objetivo

Ñython funciona como transpilador:

```text
Código Ñython -> Traducción -> Código Python -> Ejecución
```

Esto permite mantener compatibilidad con el ecosistema de Python y ofrecer una primera experiencia más cercana para estudiantes, docentes y desarrolladores hispanohablantes.

## Instalación

Requiere Python 3.10 o superior.

```bash
pip install -e .
```

Para desarrollo:

```bash
pip install -e ".[dev]"
```

Para usar IA:

```bash
pip install -e ".[ia]"
```

## Uso Básico

```bash
nython ejecutar ejemplos/hola_mundo.ny
nython traducir ejemplos/condicionales.ny
nython compilar ejemplos/funciones.ny -o funciones.py
nython version
nython ayuda
```

## Ejemplo

```nython
nombre = entrada("Escribe tu nombre: ")

si nombre == "":
    imprimir("No escribiste nada")
sino:
    imprimir("Hola " + nombre)
```

Python generado:

```python
nombre = input("Escribe tu nombre: ")

if nombre == "":
    print("No escribiste nada")
else:
    print("Hola " + nombre)
```

## Gramática Natural Inicial

```nython
para cada persona en personas:
    imprimir(persona)

repetir 3 veces:
    imprimir("Hola")

si edad esta entre 18 y 65:
    imprimir("Edad laboral")
```

## Importar Módulos `.ny`

```nython
desde matematicas importar multiplicar

resultado = multiplicar(5, 7)
imprimir(resultado)
```

El importador de Ñython traduce el módulo `.ny` antes de cargarlo.

## IA Nativa Opcional

Ñython puede integrar IA sin volverla obligatoria para el lenguaje.

Configura tu clave para OpenAI:

```powershell
setx OPENAI_API_KEY "tu_clave"
```

Usa la IA desde la CLI:

```bash
nython ia estado
nython ia preguntar "Explícame qué es un bucle"
nython ia explicar ejemplos/condicionales.ny
nython ia revisar ejemplos/funciones.ny
nython ia explicar-error ejemplos/error_nombre.ny
nython ia generar-ejercicio listas --nivel principiante
nython ia convertir-python programa.py
```

Para desarrollo, demos o pruebas sin credenciales:

```bash
nython ia estado --proveedor simulado
nython ia preguntar "Explícame una lista" --proveedor simulado
```

O desde un archivo `.ny`:

```nython
respuesta = preguntar_ia("Explícame qué hace range en Python")
imprimir(respuesta)
```

La integración usa OpenAI por defecto cuando `OPENAI_API_KEY` está configurada. El resto de Ñython funciona sin IA, sin internet y sin credenciales.

Consulta [Privacidad e IA](docs/privacidad-ia.md) antes de enviar código a un proveedor externo.

## Equivalencias Iniciales

| Español | Python |
| --- | --- |
| si | if |
| sino | else |
| osi | elif |
| para | for |
| mientras | while |
| en | in |
| funcion / definir | def |
| retornar | return |
| verdadero | True |
| falso | False |
| nulo | None |
| y | and |
| o | or |
| no | not |
| clase | class |
| importar | import |
| desde | from |
| como | as |
| intentar | try |
| excepto | except |
| finalmente | finally |
| con | with |
| romper | break |
| continuar | continue |
| pasar | pass |

## Alias Comunes

| Español | Python |
| --- | --- |
| imprimir | print |
| entrada | input |
| rango | range |
| longitud | len |
| entero | int |
| decimal | float |
| texto | str |
| booleano | bool |
| lista | list |
| tupla | tuple |
| conjunto | set |
| diccionario | dict |
| enumerar | enumerate |
| zippear | zip |
| sumar | sum |
| maximo | max |
| minimo | min |
| absoluto | abs |
| redondear | round |
| ordenado | sorted |
| tipo | type |
| abrir | open |
| preguntar_ia | función IA opcional |

## Seguridad

Ñython ejecuta código Python generado internamente. No ejecutes archivos `.ny` de fuentes desconocidas.

Esta primera versión no implementa un sandbox de seguridad.

## Pruebas

```bash
pytest
ruff check .
coverage run -m pytest
coverage report
```

## Estructura

```text
nython/              paquete principal
ejemplos/            programas de ejemplo
tests/               pruebas automatizadas
docs/                documentación inicial
vscode-extension/    base de extensión para VS Code
```

## Roadmap

### Fase 1 - MVP

- Transpilador básico.
- CLI funcional.
- Alias en español.
- Errores amigables.
- Ejemplos.
- Pruebas.
- Importador inicial para archivos `.ny`.
- Gramática natural inicial.
- IA nativa opcional por CLI y alias `preguntar_ia`.

### Fase 2 - VS Code

- Extensión completa.
- Resaltado.
- Snippets iniciales.
- Ejecución con botón.
- Comandos para ejecutar, traducir y compilar.

### Fase 3 - IA Educativa

- Tutor interactivo.
- Explicación de errores con IA.
- Generación guiada de ejercicios.
- Proveedores intercambiables.
- Conversión asistida de Python a Ñython.

### Fase 4 - Gramática Natural Avanzada

- Más expresiones cercanas al español cotidiano.
- Diagnósticos cuando una frase natural sea ambigua.

### Fase 5 - Distribución Educativa

- Documentación completa.
- Curso básico.
- Web oficial.
- Instaladores para Windows, Linux y macOS.

## Contribuir

Las contribuciones son bienvenidas. Puedes abrir issues, proponer nuevas equivalencias, mejorar documentación, agregar pruebas o trabajar en la extensión de VS Code.
