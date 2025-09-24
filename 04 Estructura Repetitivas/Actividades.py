'''1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea. '''
i = 0
while i <= 100:
    print(i)
    i += 1






'''2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
dígitos que contiene. '''
numero = int(input("Ingrese un número: "))
contador = 0
num_temp = abs(numero)
if num_temp == 0:
  contador = 1
else:
  while num_temp > 0:
    num_temp //= 10
    contador += 1
print(f"El número {numero} tiene {contador} dígitos.")





'''3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
dados por el usuario, excluyendo esos dos valores.'''
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
inicio = min(num1, num2) + 1
fin = max(num1, num2)
suma = 0
i = inicio
while i < fin:
  suma += i
  i += 1
print(f"La suma de los números entre {num1} y {num2} (excluyéndolos) es: {suma}")





'''4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
un 0. '''
total = 0
while True:
  n = int(input("Ingrese un número (0 para terminar): "))
  if n == 0:
    break
  total += n
print(f"La suma total es: {total}")






'''5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
programa debe mostrar cuántos intentos fueron necesarios para acertar el número.'''
import random
secreto = random.randint(0, 9)
intentos = 0
while True:
  intento = int(input("Adivina el número (entre 0 y 9): "))
  intentos += 1
  if intento == secreto:
    print(f"¡Correcto! El número era {secreto}. Lo lograste en {intentos} intentos.")
    break






'''6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
entre 0 y 100, en orden decreciente.'''
i = 100
while i >= 0:
  if i % 2 == 0:
    print(i)
  i -= 1







'''7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
número entero positivo indicado por el usuario. '''
limite = int(input("Ingrese un número entero positivo: "))
suma = 0
i = 0
while i <= limite:
  suma += i
  i += 1
print(f"La suma de los números entre 0 y {limite} es: {suma}")






'''8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
menor, pero debe estar preparado para procesar 100 números con un solo cambio). '''
cantidad = 100  # Cambia este valor para probar con menos números
pares = 0
impares = 0
positivos = 0
negativos = 0
contador = 0
while contador < cantidad:
  n = int(input(f"Ingrese el número {contador+1}: "))
  if n % 2 == 0:
    pares += 1
  else:
    impares += 1
  if n > 0:
    positivos += 1
  elif n < 0:
    negativos += 1
  contador += 1
print(f"Pares: {pares}, Impares: {impares}, Positivos: {positivos}, Negativos: {negativos}")







'''9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
poder procesar 100 números cambiando solo un valor).'''
cantidad = 100  # Cambia este valor para probar con menos números
suma = 0
contador = 0
while contador < cantidad:
  n = int(input(f"Ingrese el número {contador+1}: "))
  suma += n
  contador += 1
media = suma / cantidad
print(f"La media de los {cantidad} números es: {media}")







'''10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.'''
numero = int(input("Ingrese un número: "))
invertido = 0
num_temp = abs(numero)
while num_temp > 0:
  invertido = invertido * 10 + num_temp % 10
  num_temp //= 10
if numero < 0:
  invertido = -invertido
print(f"El número invertido es: {invertido}")