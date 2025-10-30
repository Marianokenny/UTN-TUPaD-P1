"""Conjunto de ejercicios introductorios a la recursividad."""

from __future__ import annotations

from functools import lru_cache
from typing import List


SEPARADOR = "=" * 64


def factorial(n: int) -> int:
	if n < 0:
		raise ValueError("El factorial solo esta definido para enteros no negativos")
	if n in (0, 1):
		return 1
	return n * factorial(n - 1)


def factoriales_hasta(n: int) -> List[int]:
	if n < 1:
		raise ValueError("El valor debe ser un entero mayor o igual a 1")
	return [factorial(valor) for valor in range(1, n + 1)]


@lru_cache(maxsize=None)
def fibonacci(posicion: int) -> int:
	if posicion < 0:
		raise ValueError("La posicion debe ser un entero no negativo")
	if posicion in (0, 1):
		return posicion
	return fibonacci(posicion - 1) + fibonacci(posicion - 2)


def serie_fibonacci(hasta: int) -> List[int]:
	if hasta < 0:
		raise ValueError("La posicion maxima debe ser un entero no negativo")
	return [fibonacci(indice) for indice in range(hasta + 1)]


def potencia(base: float, exponente: int) -> float:
	if base == 0 and exponente < 0:
		raise ValueError("No se puede elevar cero a un exponente negativo")
	if exponente == 0:
		return 1.0
	if exponente < 0:
		return 1.0 / potencia(base, -exponente)
	return base * potencia(base, exponente - 1)


def decimal_a_binario(numero: int) -> str:
	if numero < 0:
		raise ValueError("El numero debe ser entero positivo")
	if numero < 2:
		return str(numero)
	return decimal_a_binario(numero // 2) + str(numero % 2)


def es_palindromo(palabra: str) -> bool:
	if len(palabra) <= 1:
		return True
	if palabra[0] != palabra[-1]:
		return False
	return es_palindromo(palabra[1:-1])


def suma_digitos(numero: int) -> int:
	if numero < 0:
		raise ValueError("El numero debe ser entero positivo")
	if numero < 10:
		return numero
	return numero % 10 + suma_digitos(numero // 10)


def contar_bloques(nivel_base: int) -> int:
	if nivel_base < 0:
		raise ValueError("El numero de bloques debe ser entero positivo")
	if nivel_base <= 1:
		return max(nivel_base, 0)
	return nivel_base + contar_bloques(nivel_base - 1)


def contar_digito(numero: int, digito: int) -> int:
	if numero < 0:
		raise ValueError("El numero debe ser entero positivo")
	if not 0 <= digito <= 9:
		raise ValueError("El digito debe estar entre 0 y 9")
	if numero == 0:
		return 1 if digito == 0 else 0
	coincidencia = 1 if numero % 10 == digito else 0
	if numero < 10:
		return coincidencia
	return coincidencia + contar_digito(numero // 10, digito)


def pedir_entero(mensaje: str, minimo: int | None = None) -> int:
	while True:
		try:
			valor = int(input(mensaje))
			if minimo is not None and valor < minimo:
				print(f"Ingrese un valor mayor o igual a {minimo}.")
				continue
			return valor
		except ValueError:
			print("Entrada invalida. Debe ingresar un numero entero.")


def mostrar_menu() -> None:
	print("\n" + SEPARADOR)
	print("EJERCICIOS DE RECURSIVIDAD")
	print(SEPARADOR)
	print("1. Factorial de 1 hasta n")
	print("2. Serie de Fibonacci hasta n")
	print("3. Potencia base^exponente")
	print("4. Convertir decimal a binario")
	print("5. Verificar palindromo")
	print("6. Suma de digitos")
	print("7. Contar bloques de piramide")
	print("8. Contar ocurrencias de un digito")
	print("9. Salir")
	print("-" * 64)


def ejecutar_opcion(opcion: str) -> bool:
	if opcion == "1":
		limite = pedir_entero("Ingrese el numero tope (>=1): ", minimo=1)
		resultados = factoriales_hasta(limite)
		for indice, valor in enumerate(resultados, start=1):
			print(f"Factorial de {indice}: {valor}")
	elif opcion == "2":
		limite = pedir_entero("Ingrese la posicion maxima (>=0): ", minimo=0)
		serie = serie_fibonacci(limite)
		print(f"Serie de Fibonacci hasta la posicion {limite}: {serie}")
	elif opcion == "3":
		base = float(input("Ingrese la base: "))
		exponente = pedir_entero("Ingrese el exponente (entero): ")
		print(f"Resultado: {potencia(base, exponente)}")
	elif opcion == "4":
		numero = pedir_entero("Ingrese un numero decimal positivo: ", minimo=0)
		print(f"Representacion binaria: {decimal_a_binario(numero)}")
	elif opcion == "5":
		palabra = input("Ingrese una palabra sin espacios ni tildes: ").strip()
		print(f"Es palindromo: {es_palindromo(palabra)}")
	elif opcion == "6":
		numero = pedir_entero("Ingrese un entero positivo: ", minimo=0)
		print(f"Suma de digitos: {suma_digitos(numero)}")
	elif opcion == "7":
		nivel = pedir_entero("Ingrese bloques en el nivel base (>=0): ", minimo=0)
		print(f"Total de bloques necesarios: {contar_bloques(nivel)}")
	elif opcion == "8":
		numero = pedir_entero("Ingrese un entero positivo: ", minimo=0)
		digito = pedir_entero("Ingrese el digito a contar (0-9): ")
		print(f"Ocurrencias del digito {digito}: {contar_digito(numero, digito)}")
	elif opcion == "9":
		print("Hasta luego.")
		return False
	else:
		print("Opcion invalida. Seleccione un numero del 1 al 9.")
	return True


def main() -> None:
	while True:
		mostrar_menu()
		if not ejecutar_opcion(input("Elija una opcion: ").strip()):
			break


if __name__ == "__main__":
	main()
