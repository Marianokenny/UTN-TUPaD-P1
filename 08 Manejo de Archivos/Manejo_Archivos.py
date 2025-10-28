"""Práctica de manejo de archivos de texto para gestionar productos.

El programa cubre los ejercicios propuestos:
1. Crear un archivo inicial con productos de ejemplo.
2. Leer el archivo y mostrar los productos en pantalla.
3. Agregar nuevos productos ingresados por teclado sin borrar lo existente.
4. Cargar los productos en una lista de diccionarios.
5. Buscar un producto por nombre en la lista cargada.
6. Guardar los productos actualizados sobrescribiendo el archivo.

También se incluyen opciones auxiliares para ejecutar todo el práctico en orden
y para mostrar el contenido literal del archivo. Todas las operaciones validan
casos comunes: archivo ausente, formato inválido, valores incorrectos, etc.
"""

from __future__ import annotations

import os
from typing import List, Optional, TypedDict



class Producto(TypedDict):
    nombre: str
    precio: float
    cantidad: int


ARCHIVO_PRODUCTOS = "productos.txt"
SEPARADOR = "=" * 70


def crear_archivo_inicial() -> None:
    """Crear ``productos.txt`` con tres productos de ejemplo."""

    print(SEPARADOR)
    print("EJERCICIO 1 · Crear archivo inicial con productos")
    print(SEPARADOR)

    productos_iniciales = [
        {"nombre": "Lapicera", "precio": 120.5, "cantidad": 30},
        {"nombre": "Cuaderno", "precio": 250.0, "cantidad": 15},
        {"nombre": "Borrador", "precio": 45.0, "cantidad": 50},
    ]

    try:
        with open(ARCHIVO_PRODUCTOS, "w", encoding="utf-8") as archivo:
            for producto in productos_iniciales:
                archivo.write(
                    f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
                )
        print("Archivo creado con los productos iniciales.")
    except OSError as error:
        print(f"No se pudo crear el archivo: {error}")


def _leer_productos_desde_archivo() -> List[Producto]:
    """Leer ``productos.txt`` y devolver una lista de diccionarios."""

    productos: List[Producto] = []

    if not os.path.exists(ARCHIVO_PRODUCTOS):
        print("El archivo productos.txt no existe. Ejecute primero el ejercicio 1.")
        return productos

    try:
        with open(ARCHIVO_PRODUCTOS, "r", encoding="utf-8") as archivo:
            for numero_linea, linea in enumerate(archivo, 1):
                linea_limpia = linea.strip()
                if not linea_limpia:
                    continue

                partes = [parte.strip() for parte in linea_limpia.split(",")]
                if len(partes) != 3:
                    print(
                        f"Línea {numero_linea} ignorada por formato inválido: {linea_limpia}"
                    )
                    continue

                nombre, precio_str, cantidad_str = partes

                try:
                    precio = float(precio_str)
                    cantidad = int(cantidad_str)
                except ValueError:
                    print(
                        f"Línea {numero_linea} ignorada por datos inválidos: {linea_limpia}"
                    )
                    continue

                productos.append(
                    Producto(
                        nombre=nombre,
                        precio=precio,
                        cantidad=cantidad,
                    )
                )
    except OSError as error:
        print(f"No se pudo leer el archivo: {error}")

    return productos


def leer_y_mostrar_productos() -> List[Producto]:
    """Mostrar los productos almacenados y devolverlos en una lista."""

    print(SEPARADOR)
    print("EJERCICIO 2 · Leer y mostrar productos")
    print(SEPARADOR)

    productos = _leer_productos_desde_archivo()
    if not productos:
        print("No hay productos para mostrar.")
        return productos

    for indice, producto in enumerate(productos, 1):
        print(
            f"{indice}. Producto: {producto['nombre']} | Precio: ${producto['precio']:.2f}"
            f" | Cantidad: {producto['cantidad']}"
        )

    return productos


def _leer_precio_desde_teclado() -> float:
    while True:
        valor = input("Ingrese el precio del producto: ").strip()
        try:
            return float(valor)
        except ValueError:
            print("Precio inválido. Ingrese un número, use punto para decimales.")


def _leer_cantidad_desde_teclado() -> int:
    while True:
        valor = input("Ingrese la cantidad del producto: ").strip()
        try:
            return int(valor)
        except ValueError:
            print("Cantidad inválida. Ingrese un número entero.")


def agregar_producto_desde_teclado() -> None:
    """Solicitar un producto por teclado y agregarlo al archivo."""

    print(SEPARADOR)
    print("EJERCICIO 3 · Agregar producto desde teclado")
    print(SEPARADOR)

    nombre = input("Ingrese el nombre del producto: ").strip()
    if not nombre:
        print("No se ingresó nombre. Operación cancelada.")
        return

    precio = _leer_precio_desde_teclado()
    cantidad = _leer_cantidad_desde_teclado()

    try:
        with open(ARCHIVO_PRODUCTOS, "a", encoding="utf-8") as archivo:
            archivo.write(f"{nombre},{precio},{cantidad}\n")
        print(f"Producto '{nombre}' agregado correctamente.")
    except OSError as error:
        print(f"No se pudo agregar el producto: {error}")


def cargar_productos_en_lista() -> List[Producto]:
    """Cargar los productos del archivo en una lista de diccionarios."""

    print(SEPARADOR)
    print("EJERCICIO 4 · Cargar productos en una lista")
    print(SEPARADOR)

    productos = _leer_productos_desde_archivo()
    if productos:
        print(f"Se cargaron {len(productos)} productos en memoria.")
    else:
        print("No se cargaron productos.")

    return productos


def buscar_producto_por_nombre(productos: List[Producto]) -> Optional[Producto]:
    """Buscar un producto por nombre dentro de la lista cargada."""

    print(SEPARADOR)
    print("EJERCICIO 5 · Buscar producto por nombre")
    print(SEPARADOR)

    if not productos:
        print("No hay productos cargados en memoria. Use primero la opción 4.")
        return None

    nombre_buscar = input("Ingrese el nombre del producto a buscar: ").strip()
    if not nombre_buscar:
        print("No se ingresó nombre.")
        return None

    for producto in productos:
        if producto["nombre"].lower() == nombre_buscar.lower():
            print("Producto encontrado:")
            print(f"Nombre: {producto['nombre']}")
            print(f"Precio: ${producto['precio']:.2f}")
            print(f"Cantidad: {producto['cantidad']}")
            return producto

    print(f"El producto '{nombre_buscar}' no se encuentra en la lista.")
    return None


def guardar_productos_actualizados(productos: List[Producto]) -> None:
    """Sobrescribir el archivo con el estado actual de la lista de productos."""

    print(SEPARADOR)
    print("EJERCICIO 6 · Guardar productos actualizados")
    print(SEPARADOR)

    if not productos:
        print("No hay productos para guardar. Cargue o agregue productos primero.")
        return

    try:
        with open(ARCHIVO_PRODUCTOS, "w", encoding="utf-8") as archivo:
            for producto in productos:
                archivo.write(
                    f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
                )
        print(f"Se guardaron {len(productos)} productos en {ARCHIVO_PRODUCTOS}.")
    except OSError as error:
        print(f"No se pudo guardar el archivo: {error}")


def mostrar_contenido_archivo() -> None:
    """Imprimir el contenido literal del archivo si existe."""

    print(SEPARADOR)
    print("Contenido actual de productos.txt")
    print(SEPARADOR)

    if not os.path.exists(ARCHIVO_PRODUCTOS):
        print("El archivo todavía no fue creado.")
        return

    try:
        with open(ARCHIVO_PRODUCTOS, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()

        if contenido.strip():
            print(contenido)
        else:
            print("El archivo está vacío.")
    except OSError as error:
        print(f"No se pudo leer el archivo: {error}")


def ejecutar_todos_los_ejercicios() -> List[Producto]:
    """Ejecutar automáticamente todos los ejercicios en orden lógico."""

    print(SEPARADOR)
    print("EJECUCIÓN AUTOMÁTICA DEL PRÁCTICO")
    print(SEPARADOR)

    crear_archivo_inicial()
    leer_y_mostrar_productos()
    productos = cargar_productos_en_lista()

    if productos:
        primer_producto = productos[0]
        print(
            "Ejemplo de búsqueda automática del primer producto registrado: "
            f"{primer_producto['nombre']}"
        )
        print("Producto encontrado:")
        print(f"Nombre: {primer_producto['nombre']}")
        print(f"Precio: ${primer_producto['precio']:.2f}")
        print(f"Cantidad: {primer_producto['cantidad']}")

    guardar_productos_actualizados(productos)
    return productos


def mostrar_menu() -> None:
    print("\n" + SEPARADOR)
    print("PRÁCTICA · MANEJO DE ARCHIVOS DE PRODUCTOS")
    print(SEPARADOR)
    print("1. Crear archivo inicial con productos")
    print("2. Leer y mostrar productos")
    print("3. Agregar producto desde teclado")
    print("4. Cargar productos en lista de diccionarios")
    print("5. Buscar producto por nombre")
    print("6. Guardar productos actualizados")
    print("7. Ejecutar todos los ejercicios en secuencia")
    print("8. Mostrar contenido literal del archivo")
    print("9. Salir")
    print("-" * 70)


def main() -> None:
    productos_cache: List[Producto] = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-9): ").strip()

        if opcion == "1":
            crear_archivo_inicial()
            productos_cache = []
        elif opcion == "2":
            productos_cache = leer_y_mostrar_productos()
        elif opcion == "3":
            agregar_producto_desde_teclado()
            productos_cache = []
        elif opcion == "4":
            productos_cache = cargar_productos_en_lista()
        elif opcion == "5":
            if not productos_cache:
                productos_cache = cargar_productos_en_lista()
            buscar_producto_por_nombre(productos_cache)
        elif opcion == "6":
            if not productos_cache:
                productos_cache = cargar_productos_en_lista()
            guardar_productos_actualizados(productos_cache)
        elif opcion == "7":
            productos_cache = ejecutar_todos_los_ejercicios()
        elif opcion == "8":
            mostrar_contenido_archivo()
        elif opcion == "9":
            print("Hasta luego.")
            break
        else:
            print("Opción inválida. Elija un número del 1 al 9.")


if __name__ == "__main__":
    main()
