# ===============================================================================
# EJERCICIOS DE FUNCIONES - UTN PROGRAMACIÓN I
# ===============================================================================

# ===============================================================================
# EJERCICIO 1: Función imprimir_hola_mundo
# ===============================================================================
def imprimir_hola_mundo():
    """Función que imprime 'Hola Mundo!' por pantalla"""
    print("Hola Mundo!")

# ===============================================================================
# EJERCICIO 2: Función saludar_usuario
# ===============================================================================
def saludar_usuario(nombre):
    """Función que recibe un nombre y devuelve un saludo personalizado"""
    return f"Hola {nombre}!"

# ===============================================================================
# EJERCICIO 3: Función informacion_personal
# ===============================================================================
def informacion_personal(nombre, apellido, edad, residencia):
    """Función que imprime información personal completa"""
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# ===============================================================================
# EJERCICIO 4: Funciones para cálculos de círculo
# ===============================================================================
import math

def calcular_area_circulo(radio):
    """Función que calcula el área de un círculo dado su radio"""
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    """Función que calcula el perímetro de un círculo dado su radio"""
    return 2 * math.pi * radio

# ===============================================================================
# EJERCICIO 5: Función conversión segundos a horas
# ===============================================================================
def segundos_a_horas(segundos):
    """Función que convierte segundos a horas"""
    return segundos / 3600

# ===============================================================================
# EJERCICIO 6: Función tabla de multiplicar
# ===============================================================================
def tabla_multiplicar(numero):
    """Función que imprime la tabla de multiplicar de un número del 1 al 10"""
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# ===============================================================================
# EJERCICIO 7: Función operaciones básicas
# ===============================================================================
def operaciones_basicas(a, b):
    """Función que realiza operaciones básicas y devuelve una tupla con los resultados"""
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por cero"
    return (suma, resta, multiplicacion, division)

# ===============================================================================
# EJERCICIO 8: Función calcular IMC
# ===============================================================================
def calcular_imc(peso, altura):
    """Función que calcula el Índice de Masa Corporal (IMC)"""
    return peso / (altura ** 2)

# ===============================================================================
# EJERCICIO 9: Función conversión Celsius a Fahrenheit
# ===============================================================================
def celsius_a_fahrenheit(celsius):
    """Función que convierte grados Celsius a Fahrenheit"""
    return (celsius * 9/5) + 32

# ===============================================================================
# EJERCICIO 10: Función calcular promedio
# ===============================================================================
def calcular_promedio(a, b, c):
    """Función que calcula el promedio de tres números"""
    return (a + b + c) / 3

# ===============================================================================
# PROGRAMA PRINCIPAL - EJECUCIÓN DE TODOS LOS EJERCICIOS
# ===============================================================================

print("=" * 80)
print("EJERCICIOS DE FUNCIONES - UTN PROGRAMACIÓN I")
print("=" * 80)

# ===============================================================================
# EJERCICIO 1 - Ejecutar función imprimir_hola_mundo
# ===============================================================================
print("\n--- EJERCICIO 1: Función imprimir_hola_mundo ---")
imprimir_hola_mundo()

# ===============================================================================
# EJERCICIO 2 - Ejecutar función saludar_usuario
# ===============================================================================
print("\n--- EJERCICIO 2: Función saludar_usuario ---")
nombre = input("Ingrese su nombre: ")
saludo = saludar_usuario(nombre)
print(saludo)

# ===============================================================================
# EJERCICIO 3 - Ejecutar función informacion_personal
# ===============================================================================
print("\n--- EJERCICIO 3: Función informacion_personal ---")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su lugar de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

# ===============================================================================
# EJERCICIO 4 - Ejecutar funciones de círculo
# ===============================================================================
print("\n--- EJERCICIO 4: Cálculos de círculo ---")
radio = float(input("Ingrese el radio del círculo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print(f"Área del círculo: {area:.2f}")
print(f"Perímetro del círculo: {perimetro:.2f}")

# ===============================================================================
# EJERCICIO 5 - Ejecutar función segundos_a_horas
# ===============================================================================
print("\n--- EJERCICIO 5: Conversión segundos a horas ---")
segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos_a_horas(segundos)
print(f"{segundos} segundos equivalen a {horas:.2f} horas")

# ===============================================================================
# EJERCICIO 6 - Ejecutar función tabla_multiplicar
# ===============================================================================
print("\n--- EJERCICIO 6: Tabla de multiplicar ---")
numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)

# ===============================================================================
# EJERCICIO 7 - Ejecutar función operaciones_basicas
# ===============================================================================
print("\n--- EJERCICIO 7: Operaciones básicas ---")
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
suma, resta, multiplicacion, division = operaciones_basicas(a, b)
print(f"Suma: {a} + {b} = {suma}")
print(f"Resta: {a} - {b} = {resta}")
print(f"Multiplicación: {a} × {b} = {multiplicacion}")
print(f"División: {a} ÷ {b} = {division}")

# ===============================================================================
# EJERCICIO 8 - Ejecutar función calcular_imc
# ===============================================================================
print("\n--- EJERCICIO 8: Cálculo de IMC ---")
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
imc = calcular_imc(peso, altura)
print(f"Su IMC es: {imc:.2f}")

# ===============================================================================
# EJERCICIO 9 - Ejecutar función celsius_a_fahrenheit
# ===============================================================================
print("\n--- EJERCICIO 9: Conversión Celsius a Fahrenheit ---")
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")

# ===============================================================================
# EJERCICIO 10 - Ejecutar función calcular_promedio
# ===============================================================================
print("\n--- EJERCICIO 10: Cálculo de promedio ---")
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
promedio = calcular_promedio(num1, num2, num3)
print(f"El promedio de {num1}, {num2} y {num3} es: {promedio:.2f}")

print("\n" + "=" * 80)
print("TODOS LOS EJERCICIOS COMPLETADOS")
print("=" * 80)