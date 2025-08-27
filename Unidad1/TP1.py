# TP 1 - Estructuras Secuenciales (UTN a distancia)

# =============================
# Ejercicio 1: Hola Mundo


print("Hola Mundo!")

# =============================
# Ejercicio 2: Saludo con nombre

nombre = input("Ingresa tu nombre: ")
print("Hola", nombre)

# =============================
# Ejercicio 3: Presentacion completa
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} anos y vivo en {residencia}")

# =============================
# Ejercicio 4: Area y perimetro de un circulo

import math
radio = float(input("Ingresa el radio del circulo: "))
area = math.pi * radio**2
perimetro = 2 * math.pi * radio
print("Area:", area)
print("Perimetro:", perimetro)

# =============================
# Ejercicio 5: Segundos a horas

segundos = int(input("Ingresa la cantidad de segundos: "))
horas = segundos / 3600
print("Equivale a", horas, "horas")

# =============================
# Ejercicio 6: Tabla de multiplicar

n = int(input("Ingresa un numero: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)

# =============================
# Ejercicio 7: Operaciones con dos enteros distintos de 0


a = int(input("Ingresa el primer numero (=0): "))
b = int(input("Ingresa el segundo numero (=0): "))
print("Suma:", a+b)
print("Resta:", a-b)
print("Multiplicacion:", a*b)
print("Division:", a/b)

# =============================
# Ejercicio 8: Indice de masa corporal

peso = float(input("Ingresa tu peso (kg): "))
altura = float(input("Ingresa tu altura (m): "))
imc = peso / (altura**2)
print("Tu IMC es:", imc)

# =============================
# Ejercicio 9: Celsius a Fahrenheit


celsius = float(input("Ingresa la temperatura en °C: "))
fahrenheit = (9/5) * celsius + 32
print("Equivalente en °F:", fahrenheit)

# =============================
# Ejercicio 10: Promedio de 3 numeros

n1 = float(input("Ingresa el primer numero: "))
n2 = float(input("Ingresa el segundo numero: "))
n3 = float(input("Ingresa el tercer numero: "))
promedio = (n1 + n2 + n3) / 3
print("El promedio es:", promedio)
