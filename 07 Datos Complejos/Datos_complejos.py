# ===============================================================================
# EJERCICIO 1: Agregar frutas al diccionario
# ===============================================================================
def ejercicio_1():
    """Dado el diccionario precios_frutas, añadir las frutas especificadas"""
    print("=" * 60)
    print("EJERCICIO 1: Agregar frutas al diccionario")
    print("=" * 60)
    
    # Diccionario inicial
    precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
    print(f"Diccionario inicial: {precios_frutas}")
    
    # Añadir las nuevas frutas
    precios_frutas['Naranja'] = 1200
    precios_frutas['Manzana'] = 1500
    precios_frutas['Pera'] = 2300
    
    print(f"Diccionario después de agregar frutas: {precios_frutas}")
    return precios_frutas

# ===============================================================================
# EJERCICIO 2: Actualizar precios de frutas
# ===============================================================================
def ejercicio_2(precios_frutas):
    """Actualizar los precios de las frutas especificadas"""
    print("\n" + "=" * 60)
    print("EJERCICIO 2: Actualizar precios de frutas")
    print("=" * 60)
    
    print(f"Diccionario antes de actualizar: {precios_frutas}")
    
    # Actualizar precios
    precios_frutas['Banana'] = 1330
    precios_frutas['Manzana'] = 1700
    precios_frutas['Melón'] = 2800
    
    print(f"Diccionario después de actualizar precios: {precios_frutas}")
    return precios_frutas

# ===============================================================================
# EJERCICIO 3: Crear lista de frutas sin precios
# ===============================================================================
def ejercicio_3(precios_frutas):
    """Crear una lista que contenga únicamente las frutas sin los precios"""
    print("\n" + "=" * 60)
    print("EJERCICIO 3: Lista de frutas sin precios")
    print("=" * 60)
    
    # Crear lista solo con las claves (nombres de frutas)
    lista_frutas = list(precios_frutas.keys())
    
    print(f"Diccionario completo: {precios_frutas}")
    print(f"Lista solo con frutas: {lista_frutas}")
    return lista_frutas

# ===============================================================================
# EJERCICIO 4: Agenda telefónica
# ===============================================================================
def ejercicio_4():
    """Programa para almacenar y consultar números telefónicos"""
    print("\n" + "=" * 60)
    print("EJERCICIO 4: Agenda telefónica")
    print("=" * 60)
    
    contactos = {}
    
    # Cargar 5 contactos
    print("Ingrese 5 contactos:")
    for i in range(5):
        nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
        telefono = input(f"Ingrese el teléfono de {nombre}: ")
        contactos[nombre] = telefono
    
    print(f"\nContactos cargados: {contactos}")
    
    # Consultar contacto
    nombre_buscar = input("\nIngrese el nombre del contacto a buscar: ")
    
    if nombre_buscar in contactos:
        print(f"El teléfono de {nombre_buscar} es: {contactos[nombre_buscar]}")
    else:
        print(f"El contacto {nombre_buscar} no existe en la agenda.")
    
    return contactos

# ===============================================================================
# EJERCICIO 5: Análisis de palabras en una frase
# ===============================================================================
def ejercicio_5():
    """Analizar palabras únicas y contar ocurrencias en una frase"""
    print("\n" + "=" * 60)
    print("EJERCICIO 5: Análisis de palabras en una frase")
    print("=" * 60)
    
    # Solicitar frase al usuario
    frase = input("Ingrese una frase: ")
    
    # Convertir a minúsculas y dividir en palabras
    palabras = frase.lower().split()
    
    # Crear set de palabras únicas
    palabras_unicas = set(palabras)
    
    # Crear diccionario con recuento de palabras
    recuento = {}
    for palabra in palabras:
        if palabra in recuento:
            recuento[palabra] += 1
        else:
            recuento[palabra] = 1
    
    # Mostrar resultados
    print(f"Frase ingresada: '{frase}'")
    print(f"Palabras_unicas: {palabras_unicas}")
    print(f"Recuento: {recuento}")
    
    return palabras_unicas, recuento

# ===============================================================================
# EJERCICIO 6: Promedios de alumnos
# ===============================================================================
def ejercicio_6():
    """Ingresar nombres de 3 alumnos con sus 3 notas y calcular promedios"""
    print("\n" + "=" * 60)
    print("EJERCICIO 6: Promedios de alumnos")
    print("=" * 60)
    
    alumnos = {}
    
    # Ingresar datos de 3 alumnos
    for i in range(3):
        nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
        
        print(f"Ingrese las 3 notas de {nombre}:")
        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
        nota3 = float(input("Nota 3: "))
        
        # Guardar como tupla
        alumnos[nombre] = (nota1, nota2, nota3)
    
    # Mostrar promedios
    print("\nPromedios de los alumnos:")
    for nombre, notas in alumnos.items():
        promedio = sum(notas) / len(notas)
        print(f'"{nombre}": {notas} -> Promedio: {promedio:.2f}')
    
    return alumnos

# ===============================================================================
# EJERCICIO 7: Análisis de parciales aprobados
# ===============================================================================
def ejercicio_7():
    """Analizar estudiantes que aprobaron parciales usando sets"""
    print("\n" + "=" * 60)
    print("EJERCICIO 7: Análisis de parciales aprobados")
    print("=" * 60)
    
    # Sets de estudiantes que aprobaron cada parcial
    parcial_1 = {101, 102, 103, 104, 105, 106}
    parcial_2 = {103, 104, 105, 107, 108, 109}
    
    print(f"Estudiantes que aprobaron Parcial 1: {parcial_1}")
    print(f"Estudiantes que aprobaron Parcial 2: {parcial_2}")
    
    # Estudiantes que aprobaron ambos parciales (intersección)
    ambos_parciales = parcial_1 & parcial_2
    print(f"Aprobaron ambos parciales: {ambos_parciales}")
    
    # Estudiantes que aprobaron solo uno de los dos (diferencia simétrica)
    solo_uno = parcial_1 ^ parcial_2
    print(f"Aprobaron solo uno de los dos: {solo_uno}")
    
    # Lista total de estudiantes que aprobaron al menos un parcial (unión)
    al_menos_uno = parcial_1 | parcial_2
    print(f"Lista total de estudiantes (al menos un parcial): {al_menos_uno}")
    
    return parcial_1, parcial_2, ambos_parciales, solo_uno, al_menos_uno

# ===============================================================================
# EJERCICIO 8: Sistema de gestión de stock
# ===============================================================================
def ejercicio_8():
    """Sistema para gestionar stock de productos"""
    print("\n" + "=" * 60)
    print("EJERCICIO 8: Sistema de gestión de stock")
    print("=" * 60)
    
    # Diccionario inicial de productos
    stock = {
        "Laptop": 15,
        "Mouse": 50,
        "Teclado": 30,
        "Monitor": 8
    }
    
    print(f"Stock inicial: {stock}")
    
    while True:
        print("\n--- MENÚ ---")
        print("1. Consultar stock de un producto")
        print("2. Agregar unidades al stock")
        print("3. Agregar nuevo producto")
        print("4. Mostrar todo el stock")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            producto = input("Ingrese el nombre del producto: ")
            if producto in stock:
                print(f"Stock de {producto}: {stock[producto]} unidades")
            else:
                print(f"El producto {producto} no existe en el inventario.")
        
        elif opcion == "2":
            producto = input("Ingrese el nombre del producto: ")
            if producto in stock:
                cantidad = int(input(f"Ingrese cantidad a agregar a {producto}: "))
                stock[producto] += cantidad
                print(f"Stock actualizado. {producto}: {stock[producto]} unidades")
            else:
                print(f"El producto {producto} no existe. Use opción 3 para agregarlo.")
        
        elif opcion == "3":
            producto = input("Ingrese el nombre del nuevo producto: ")
            if producto not in stock:
                cantidad = int(input(f"Ingrese el stock inicial para {producto}: "))
                stock[producto] = cantidad
                print(f"Producto {producto} agregado con {cantidad} unidades.")
            else:
                print(f"El producto {producto} ya existe. Use opción 2 para agregar stock.")
        
        elif opcion == "4":
            print("Stock completo:")
            for producto, cantidad in stock.items():
                print(f"- {producto}: {cantidad} unidades")
        
        elif opcion == "5":
            break
        
        else:
            print("Opción inválida. Intente nuevamente.")
    
    return stock

# ===============================================================================
# EJERCICIO 9: Agenda con tuplas como claves
# ===============================================================================
def ejercicio_9():
    """Crear una agenda donde las claves sean tuplas de (día, hora)"""
    print("\n" + "=" * 60)
    print("EJERCICIO 9: Agenda con tuplas como claves")
    print("=" * 60)
    
    # Agenda de ejemplo
    agenda = {
        ("lunes", "10:00"): "Reunión",
        ("martes", "15:00"): "Clase de inglés",
        ("miércoles", "09:00"): "Dentista",
        ("jueves", "14:30"): "Entrega de proyecto",
        ("viernes", "16:00"): "Gimnasio"
    }
    
    print("Agenda actual:")
    for (dia, hora), evento in agenda.items():
        print(f'- {dia.capitalize()} a las {hora}: "{evento}"')
    
    # Consultar actividad
    dia_consulta = input("\nIngrese el día a consultar: ").lower()
    hora_consulta = input("Ingrese la hora a consultar (formato HH:MM): ")
    
    clave_busqueda = (dia_consulta, hora_consulta)
    
    if clave_busqueda in agenda:
        print(f'El {dia_consulta} a las {hora_consulta}: "{agenda[clave_busqueda]}"')
    else:
        print(f"No hay actividad programada para el {dia_consulta} a las {hora_consulta}")
    
    return agenda

# ===============================================================================
# EJERCICIO 10: Invertir diccionario países-capitales
# ===============================================================================
def ejercicio_10():
    """Construir diccionario invertido donde capitales sean claves y países valores"""
    print("\n" + "=" * 60)
    print("EJERCICIO 10: Invertir diccionario países-capitales")
    print("=" * 60)
    
    # Diccionario original
    original = {
        "Argentina": "Buenos Aires",
        "Chile": "Santiago",
        "Brasil": "Brasília",
        "Uruguay": "Montevideo",
        "Paraguay": "Asunción",
        "Bolivia": "Sucre"
    }
    
    print(f"Original: {original}")
    
    # Crear diccionario invertido
    invertido = {}
    for pais, capital in original.items():
        invertido[capital] = pais
    
    print(f'Invertido: {invertido}')
    
    return original, invertido

# ===============================================================================
# PROGRAMA PRINCIPAL
# ===============================================================================
def main():
    """Función principal que ejecuta todos los ejercicios"""
    print("*" * 80)
    print("PRÁCTICO 6: ESTRUCTURAS DE DATOS COMPLEJAS")
    print("UTN - TECNICATURA UNIVERSITARIA EN PROGRAMACIÓN")
    print("*" * 80)
    
    # Ejecutar ejercicios 1, 2 y 3 en secuencia (usan el mismo diccionario)
    precios_frutas = ejercicio_1()
    precios_frutas = ejercicio_2(precios_frutas)
    lista_frutas = ejercicio_3(precios_frutas)
    
    # Ejercicio 7: Análisis de parciales
    parcial_1, parcial_2, ambos, solo_uno, al_menos_uno = ejercicio_7()
    
    # Ejercicio 10: Invertir diccionario
    original, invertido = ejercicio_10()
    
    print("\n" + "*" * 80)
    print("EJERCICIOS COMPLETADOS AUTOMÁTICAMENTE")
    print("*" * 80)
    print("\nEJERCICIOS INTERACTIVOS (requieren input del usuario):")
    print("Para ejecutarlos, llama a las siguientes funciones:")
    print("- ejercicio_4()  # Agenda telefónica")
    print("- ejercicio_5()  # Análisis de palabras en frase")
    print("- ejercicio_6()  # Promedios de alumnos")
    print("- ejercicio_8()  # Sistema de gestión de stock")
    print("- ejercicio_9()  # Agenda con tuplas")

# ===============================================================================
# FUNCIONES INDIVIDUALES PARA EJECUTAR EJERCICIOS INTERACTIVOS
# ===============================================================================
def ejecutar_ejercicio_4():
    """Ejecutar solo el ejercicio 4 - Agenda telefónica"""
    return ejercicio_4()

def ejecutar_ejercicio_5():
    """Ejecutar solo el ejercicio 5 - Análisis de palabras"""
    return ejercicio_5()

def ejecutar_ejercicio_6():
    """Ejecutar solo el ejercicio 6 - Promedios de alumnos"""
    return ejercicio_6()

def ejecutar_ejercicio_8():
    """Ejecutar solo el ejercicio 8 - Gestión de stock"""
    return ejercicio_8()

def ejecutar_ejercicio_9():
    """Ejecutar solo el ejercicio 9 - Agenda con tuplas"""
    return ejercicio_9()

# Ejecutar el programa
if __name__ == "__main__":
    main()
