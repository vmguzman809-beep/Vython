# Privacidad e IA

La integración de IA de Ñython es opcional. El lenguaje, el traductor, la CLI básica y las pruebas funcionan sin internet y sin credenciales.

## Qué se envía a IA

Los comandos de IA pueden enviar contenido a un proveedor externo:

- `nython ia preguntar`: envía la pregunta escrita por el usuario.
- `nython ia explicar`: envía el archivo Ñython y el Python generado.
- `nython ia revisar`: envía el archivo Ñython y el Python generado.
- `nython ia explicar-error`: envía el archivo Ñython, el Python generado si existe y el error formateado. Por defecto no ejecuta el programa.
- `nython ia convertir-python`: envía el archivo Python indicado.

## Recomendaciones

- No envíes claves, tokens, datos personales ni código privado sensible.
- Usa `--proveedor simulado` para demos, clases y pruebas sin enviar nada fuera de tu equipo.
- Revisa el código antes de usar proveedores externos.
- Usa `--ejecutar` en `explicar-error` solo si aceptas ejecutar el archivo para capturar errores en tiempo de ejecución.

## Modo simulado

```bash
nython ia preguntar "Explícame una lista" --proveedor simulado
```

El proveedor simulado no usa internet, no requiere API key y no envía datos a servicios externos.
