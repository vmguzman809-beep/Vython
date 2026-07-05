# Ñython

**Programa en español. Ejecuta en Python.**

Ñython es una herramienta educativa para escribir código con sintaxis en español y ejecutarlo como Python real. No busca reemplazar Python. Busca acercar Python a millones de hispanohablantes que están aprendiendo a programar.

## Objetivo

Ñython funciona como transpilador:

```text
Código Ñython -> Traducción -> Código Python -> Ejecución
```

Esto permite mantener compatibilidad con el ecosistema de Python y, al mismo tiempo, ofrecer una primera experiencia más cercana para estudiantes, docentes y desarrolladores hispanohablantes.

## Instalación

Requiere Python 3.10 o superior.

```bash
pip install -e .
```

## Uso básico

```bash
nython ejecutar ejemplos/hola_mundo.ny
nython traducir ejemplos/condicionales.ny
nython compilar ejemplos/funciones.ny -o funciones.py
nython version
nython ayuda
```

## Ejemplos

```nython
nombre = entrada("Escribe tu nombre: ")

si nombre == "":
    imprimir("No escribiste nada")
sino:
    imprimir("Hola " + nombre)
```

Se traduce a:

```python
nombre = input("Escribe tu nombre: ")

if nombre == "":
    print("No escribiste nada")
else:
    print("Hola " + nombre)
```

## Gramática natural inicial

```nython
para cada persona en personas:
    imprimir(persona)

repetir 3 veces:
    imprimir("Hola")

si edad esta entre 18 y 65:
    imprimir("Edad laboral")
```

## Importar módulos `.ny`

Un archivo Ñython puede importar otro módulo escrito en `.ny`:

```nython
desde matematicas importar multiplicar

resultado = multiplicar(5, 7)
imprimir(resultado)
```

El importador de Ñython traduce el módulo `.ny` antes de cargarlo.

## IA nativa opcional

Ñython puede integrar IA de forma nativa sin volverla obligatoria para el lenguaje.

Instala el extra:

```bash
pip install -e ".[ia]"
```

Configura tu clave:

```powershell
setx OPENAI_API_KEY "tu_clave"
```

Usa la IA desde la CLI:

```bash
nython ia preguntar "Explícame qué es un bucle"
nython ia explicar ejemplos/condicionales.ny
nython ia revisar ejemplos/funciones.ny
```

O desde un archivo `.ny`:

```nython
respuesta = preguntar_ia("Explícame qué hace range en Python")
imprimir(respuesta)
```

La integración usa la API de OpenAI cuando `OPENAI_API_KEY` está configurada. El resto de Ñython funciona sin IA, sin internet y sin credenciales.

## Equivalencias iniciales

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

## Alias comunes

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

## Seguridad

Ñython ejecuta código Python generado internamente. No ejecutes archivos `.ny` de fuentes desconocidas.

Esta primera versión no implementa un sandbox de seguridad.

## Pruebas

```bash
pytest
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
- Autocompletado.
- Ejecución con botón.
- Snippets.

### Fase 3 - Gramática natural avanzada

- Más expresiones cercanas al español cotidiano.
- Diagnósticos cuando una frase natural sea ambigua.

### Fase 4 - Errores educativos

- Sugerencias para principiantes.
- Explicaciones simples.
- Contexto alrededor de la línea con error.

### Fase 5 - Distribución educativa

- Documentación completa.
- Curso básico.
- Web oficial.
- Instaladores para Windows, Linux y macOS.

## Contribuir

Las contribuciones son bienvenidas. Puedes abrir issues, proponer nuevas equivalencias, mejorar documentación, agregar pruebas o trabajar en la extensión de VS Code.
