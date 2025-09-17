#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga "Es mayor de edad".

# Solicitar la edad del usuario
edad = int(input("Ingrese su edad: "))

# Verificar si es mayor de edad
if edad >= 18:
    print("Es mayor de edad")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.
nota = float(input ("ingrese la nota del alumno"))
if nota >= 6:
    print("El alumno aprobo")
else:
    print("El alumno Desaprobo")

'''3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
operador de módulo (%) en Python para evaluar si un número es par o impar.'''

# Solicitar un número al usuario
numero = int(input("Ingrese un número: "))

# Verificar si es par usando el operador módulo (%)
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")
''' Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
siguientes categorías pertenece:
● Niño/a: menor de 12 años.
● Adolescente: mayor o igual que 12 años y menor que 18 años.
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
● Adulto/a: mayor o igual que 30 años'''

edad= int(input("Ingrese la edad: "))
if edad < 12:
    print("Es un Niño/a")
elif 12 <= edad < 18:
    print("Es un Adolescente")
elif 18 <= edad < 30:
    print("Es un Adulto/a joven")
elif edad >= 30:
    print("Es un Adulto/a")

'''Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
como una lista o un string.'''
contra = (input ("Ingrese su contraseña"))
if 8 <= len(contra) <= 14:
    print("Contraseña válida")
else:
    print("La contraseña debe tener entre 8 y 14 dígitos")

'''6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el
siguiente:
from statistics import mode, median, mean
mi_lista = [1,2,5,5,3]
mean(mi_lista)
En la documentación oficial se puede encontrar más información sobre este paquete:
https://docs.python.org/es/3.8/library/statistics.html.
La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
mediana es mayor que la moda.
● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
la mediana es menor que la moda.
● Sin sesgo: cuando la media, la mediana y la moda son iguales.
Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
Definir la lista numeros_aleatorios de la siguiente forma:
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
forma aleatoria.'''

# Importar las librerías necesarias
import random
from statistics import mode, median, mean

# Generar lista de 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcular moda, mediana y media
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

# Mostrar los valores calculados
print(f"Lista de números: {numeros_aleatorios}")
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media:.2f}")

# Determinar el tipo de sesgo
if media > mediana > moda:
    print("Resultado: Sesgo positivo o a la derecha")
elif media < mediana < moda:
    print("Resultado: Sesgo negativo o a la izquierda")
elif media == mediana == moda:
    print("Resultado: Sin sesgo")
else:
    print("Resultado: Los valores no siguen un patrón de sesgo claro")

'''7)Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
pantalla.'''
frase = str (input ("ingrese una frase o palabra"))
ultimo = frase[-1].lower()  # lo pasamos a minúscula para no tener problema con mayúsculas

# Verificamos si termina en vocal
if ultimo in "aeiou":
    resultado = frase + "!"
else:
    resultado = frase

# Mostramos el resultado
print("Resultado:", resultado)

'''8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
dependiendo de la opción que desee:
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
lower() y title() de Python para convertir entre mayúsculas y minúsculas'''
# Pedir el nombre al usuario
nombre = input("Ingrese su nombre: ")

# Pedir la opción
print("Elija una opción:")
print("1. Convertir el nombre a MAYÚSCULAS")
print("2. Convertir el nombre a minúsculas")
print("3. Convertir el nombre con la primera letra mayúscula")

opcion = input("Ingrese 1, 2 o 3: ")

# Estructura condicional
if opcion == "1":
    resultado = nombre.upper()
elif opcion == "2":
    resultado = nombre.lower()
elif opcion == "3":
    resultado = nombre.title()
else:
    resultado = "Opción inválida."

# Mostrar el resultado
print("Resultado:", resultado)

'''9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
por pantalla:
● Menor que 3: "Muy leve" (imperceptible).
● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
generalmente no causa daños).
● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
débiles).
● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
'''
# Pedimos la magnitud al usuario
magnitud = float(input("Ingrese la magnitud del terremoto: "))

# Clasificación según escala de Richter
if magnitud < 3:
    resultado = "Muy leve (imperceptible)."
elif magnitud >= 3 and magnitud < 4:
    resultado = "Leve (ligeramente perceptible)."
elif magnitud >= 4 and magnitud < 5:
    resultado = "Moderado (sentido por personas, pero generalmente no causa daños)."
elif magnitud >= 5 and magnitud < 6:
    resultado = "Fuerte (puede causar daños en estructuras débiles)."
elif magnitud >= 6 and magnitud < 7:
    resultado = "Muy fuerte (puede causar daños significativos)."
else:
    resultado = "Extremo (puede causar graves daños a gran escala)."

# Mostramos el resultado
print("Clasificación:", resultado)


'''10)'''
# Pedir datos al usuario
hemisferio = input("Ingrese el hemisferio (N/S): ").upper()
mes = int(input("Ingrese el número de mes (1-12): "))
dia = int(input("Ingrese el día del mes (1-31): "))

# Determinar estación según mes y día
if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    estacion_norte = "Invierno"
    estacion_sur = "Verano"

elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"

elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    estacion_norte = "Verano"
    estacion_sur = "Invierno"

else:  # desde 21 de septiembre hasta 20 de diciembre
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"

# Mostrar el resultado según hemisferio
if hemisferio == "N":
    print("Estación:", estacion_norte)
elif hemisferio == "S":
    print("Estación:", estacion_sur)
else:
    print("Hemisferio inválido, ingrese N o S.")
