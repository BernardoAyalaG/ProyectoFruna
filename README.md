# Proyecto Fruna

Este proyecto contiene un script en Python llamado `ProductoFruna.py` que simula la venta de productos de una tienda sencilla. El programa muestra una lista de productos disponibles, permite la entrada de productos por parte del usuario y genera un resumen de la factura con el total a pagar.

## Contenido

- `ProductoFruna.py`: Script principal del proyecto.

## Requisitos

- Python 3.x

## Uso

1. Abrir una terminal y cambiar al directorio del proyecto:
   ```bash
   cd c:\Users\bernardo\Desktop\ProyectoFruna
   ```
2. Ejecutar el script:
   ```bash
   python ProductoFruna.py
   ```
3. Ingresar los nombres de los productos uno por uno.
4. Escribir `ahi noma pelao` para finalizar la entrada.
5. El programa imprimirá la factura con el precio de cada producto y el total a pagar.

## Comportamiento actual

- El programa imprime los productos disponibles al inicio.
- Permite agregar productos ingresando sus nombres.
- Si el usuario no ingresa nada o ingresa solo números, muestra un mensaje de error.
- Al finalizar, muestra el detalle de la factura y el total.

## Notas importantes

- En el código actual, la clave `frunacola` está duplicada en el diccionario `Preciosfruna`, por lo que solo se conservará el último valor definido.
- El script busca los productos en el diccionario usando `producto.lower()`, por lo que la consulta es insensible a mayúsculas/minúsculas.

## Posibles mejoras

- Corregir la clave duplicada de `frunacola` en el diccionario de precios.
- Agregar validación para productos no existentes y mostrar un mensaje más claro.
- Permitir cantidades para cada producto.
- Guardar la factura en un archivo de texto.
