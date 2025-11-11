import csv
import os

def normalizar_nombre(nombre: str) -> str:                         #Devuelve el nombre en minúsculas y sin espacios redundantes.
    
    partes = nombre.split()
    texto = " ".join(partes)
    texto = texto.strip()
    texto = texto.lower()
    return texto


def convertir_entero(valor: str) -> tuple:                         #Convierte una cadena a entero.Devuelve (True, entero) si es válido, o (False, 0) si no lo es.

    valor = valor.strip()
    if valor == "":
        return False, 0
    if valor.isdigit():
        return True, int(valor)
    return False, 0


def cargar_paises(ruta_csv: str) -> tuple:                       #Carga la lista de países y sus datos desde un archivo CSV. 
    paises = []
    errores = []

    if not os.path.exists(ruta_csv):
        errores.append("Archivo '" + ruta_csv + "' no encontrado. Se inicia con lista vacía.")
        return paises, errores

    archivo = open(ruta_csv, mode="r", encoding="utf-8", newline="")
    lector = csv.DictReader(archivo)
    esperadas = ["nombre", "poblacion", "superficie", "continente"]

    if lector.fieldnames is not None:
        encabezados = []
        for h in lector.fieldnames:
            encabezados.append(h.strip().lower())
    else:
        encabezados = []

    completo = True
    for h in esperadas:
        if h not in encabezados:
            completo = False

    if not completo:
        errores.append("Encabezado CSV inválido o incompleto. Se esperan: nombre,poblacion,superficie,continente")
        archivo.close()
        return [], errores

    linea = 2
    for fila in lector:
        nombre = fila.get("nombre", "").strip()
        continente = fila.get("continente", "").strip()
        ok_pob, poblacion = convertir_entero(fila.get("poblacion", ""))
        ok_sup, superficie = convertir_entero(fila.get("superficie", ""))

        if nombre == "":
            errores.append("Fila " + str(linea) + ": nombre vacío. Fila omitida.")
        elif not ok_pob:
            errores.append("Fila " + str(linea) + ": población inválida ('" + fila.get("poblacion", "") + "'). Fila omitida.")
        elif not ok_sup:
            errores.append("Fila " + str(linea) + ": superficie inválida ('" + fila.get("superficie", "") + "'). Fila omitida.")
        else:
            paises.append({
                "nombre": " ".join(nombre.split()),
                "poblacion": poblacion,
                "superficie": superficie,
                "continente": " ".join(continente.split())
            })
        linea = linea + 1

    archivo.close()
    return paises, errores


def guardar_paises(ruta_csv: str, paises: list) -> None:                  #Guarda toda la lista de países en un archivo CSV.                                                                     
    carpeta = os.path.dirname(ruta_csv)
    if carpeta != "" and not os.path.exists(carpeta):
        os.makedirs(carpeta, exist_ok=True)

    archivo = open(ruta_csv, mode="w", encoding="utf-8", newline="")
    campos = ["nombre", "poblacion", "superficie", "continente"]
    escritor = csv.DictWriter(archivo, fieldnames=campos)
    escritor.writeheader()

    for p in paises:
        escritor.writerow({
            "nombre": p.get("nombre", ""),
            "poblacion": p.get("poblacion", 0),
            "superficie": p.get("superficie", 0),
            "continente": p.get("continente", "")
        })

    archivo.close()


def buscar_indice_pais(paises: list, nombre: str) -> int:                #Devuelve el índice de un país por su nombre, no es necesario escribirlo completo                                                                      
    nombre_normal = normalizar_nombre(nombre)
    indice = 0
    while indice < len(paises):
        nombre_lista = normalizar_nombre(paises[indice].get("nombre", ""))
        if nombre_lista == nombre_normal:
            return indice
        indice = indice + 1
    return -1


def agregar_pais(paises: list) -> bool:                                 #Agrega un nuevo país a la lista. 
    nombre = input("Nombre del país: ").strip()
    if nombre == "":
        print("El nombre no puede estar vacío.")
        return False
    if buscar_indice_pais(paises, nombre) != -1:
        print("Ya existe un país con ese nombre.")
        return False

    pob_raw = input("Población (entero): ").strip()
    ok_pob, poblacion = convertir_entero(pob_raw)
    if not ok_pob:
        print("Población inválida.")
        return False

    sup_raw = input("Superficie en km² (entero): ").strip()
    ok_sup, superficie = convertir_entero(sup_raw)
    if not ok_sup:
        print("Superficie inválida.")
        return False

    continente = input("Continente: ").strip()
    if continente == "":
        print("El continente no puede estar vacío.")
        return False

    paises.append({
        "nombre": " ".join(nombre.split()),
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": " ".join(continente.split())
    })
    print("País '" + nombre + "' agregado correctamente.")
    return True


def actualizar_pais(paises: list) -> bool:                              #Actualiza la población y superficie de un país existente.    
    nombre = input("Nombre del país a actualizar: ").strip()
    indice = buscar_indice_pais(paises, nombre)
    if indice == -1:
        print("País no encontrado.")
        return False

    pob_raw = input("Nueva población (actual " + str(paises[indice]["poblacion"]) + "): ").strip()
    ok_pob, poblacion = convertir_entero(pob_raw)
    if not ok_pob:
        print("Población inválida.")
        return False

    sup_raw = input("Nueva superficie (actual " + str(paises[indice]["superficie"]) + "): ").strip()
    ok_sup, superficie = convertir_entero(sup_raw)
    if not ok_sup:
        print("Superficie inválida.")
        return False

    paises[indice]["poblacion"] = poblacion
    paises[indice]["superficie"] = superficie
    print("País '" + paises[indice]["nombre"] + "' actualizado correctamente.")
    return True


def buscar_pais(paises: list) -> None:                                     #Busca países por coincidencia parcial en el nombre(no es necesario escribirlo completo)    
    texto = input("Buscar por nombre: ").strip()
    if texto == "":
        print("Texto vacío.")
        return

    texto_normal = normalizar_nombre(texto)
    encontrados = []
    for p in paises:
        if texto_normal in normalizar_nombre(p.get("nombre", "")):
            encontrados.append(p)

    if len(encontrados) == 0:
        print("No se encontraron países.")
    else:
        for p in encontrados:
            print("- " + p["nombre"] + ": población=" + str(p["poblacion"]) +
                  ", superficie=" + str(p["superficie"]) +
                  ", continente=" + p["continente"])


def filtrar_por_continente(paises: list) -> None:                          #Muestra países de un continente específico    
    cont = input("Ingrese continente: ").strip()
    if cont == "":
        print("El continente no puede estar vacío.")
        return

    cont_norm = normalizar_nombre(cont)
    resultado = []
    for p in paises:
        if normalizar_nombre(p.get("continente", "")) == cont_norm:
            resultado.append(p)

    if len(resultado) == 0:
        print("No hay países en ese continente.")
    else:
        for p in resultado:
            print("- " + p["nombre"] + ": población=" + str(p["poblacion"]) +
                  ", superficie=" + str(p["superficie"]))


def filtrar_por_rango(paises: list, campo: str, etiqueta: str) -> None:      #Filtra países por un rango de valores.    
    minimo_txt = input(etiqueta + " mínima: ").strip()
    maximo_txt = input(etiqueta + " máxima: ").strip()
    ok_min, minimo = convertir_entero(minimo_txt)
    ok_max, maximo = convertir_entero(maximo_txt)

    if not ok_min or not ok_max or minimo > maximo:
        print("Rango inválido.")
        return

    resultado = []
    indice = 0
    while indice < len(paises):
        valor = paises[indice].get(campo, 0)
        if valor >= minimo and valor <= maximo:
            resultado.append(paises[indice])
        indice = indice + 1

    if len(resultado) == 0:
        print("No hay países en ese rango.")
    else:
        for p in resultado:
            print("- " + p["nombre"] + ": " + etiqueta.lower() + "=" + str(p[campo]))


def ordenar_paises(paises: list) -> None:                                    #Ordena la lista de países según la opción del usuario.    
    print("Ordenar por: 1-Nombre, 2-Población, 3-Superficie")
    opcion = input("Opción (1-3): ").strip()
    orden = input("Orden: A-Ascendente / D-Descendente: ").strip().upper()

    if opcion == "1":
        for i in range(len(paises) - 1):
            for j in range(i + 1, len(paises)):
                if orden == "D":
                    if normalizar_nombre(paises[i]["nombre"]) < normalizar_nombre(paises[j]["nombre"]):
                        temp = paises[i]
                        paises[i] = paises[j]
                        paises[j] = temp
                else:
                    if normalizar_nombre(paises[i]["nombre"]) > normalizar_nombre(paises[j]["nombre"]):
                        temp = paises[i]
                        paises[i] = paises[j]
                        paises[j] = temp
    elif opcion == "2":
        for i in range(len(paises) - 1):
            for j in range(i + 1, len(paises)):
                if orden == "D":
                    if paises[i]["poblacion"] < paises[j]["poblacion"]:
                        temp = paises[i]
                        paises[i] = paises[j]
                        paises[j] = temp
                else:
                    if paises[i]["poblacion"] > paises[j]["poblacion"]:
                        temp = paises[i]
                        paises[i] = paises[j]
                        paises[j] = temp
    elif opcion == "3":
        for i in range(len(paises) - 1):
            for j in range(i + 1, len(paises)):
                if orden == "D":
                    if paises[i]["superficie"] < paises[j]["superficie"]:
                        temp = paises[i]
                        paises[i] = paises[j]
                        paises[j] = temp
                else:
                    if paises[i]["superficie"] > paises[j]["superficie"]:
                        temp = paises[i]
                        paises[i] = paises[j]
                        paises[j] = temp
    else:
        print("Opción inválida.")
        return

    for p in paises:
        print("- " + p["nombre"] + ": población=" + str(p["poblacion"]) + ", superficie=" + str(p["superficie"]))


def estadisticas(paises: list) -> None:       #Muestra estadísticas generales del conjunto de países.    
    if len(paises) == 0:
        print("No hay datos cargados.")
        return

    max_p = paises[0]
    min_p = paises[0]
    suma_p = 0
    suma_s = 0
    por_cont = {}

    for p in paises:
        suma_p = suma_p + p["poblacion"]
        suma_s = suma_s + p["superficie"]

        if p["poblacion"] > max_p["poblacion"]:
            max_p = p
        if p["poblacion"] < min_p["poblacion"]:
            min_p = p

        cont = p["continente"]
        if cont in por_cont:
            por_cont[cont] = por_cont[cont] + 1
        else:
            por_cont[cont] = 1

    promedio_p = suma_p / len(paises)
    promedio_s = suma_s / len(paises)

    print("País con mayor población: " + max_p["nombre"] + " (" + str(max_p["poblacion"]) + ")")
    print("País con menor población: " + min_p["nombre"] + " (" + str(min_p["poblacion"]) + ")")
    print("Promedio de población: " + str(round(promedio_p, 2)))
    print("Promedio de superficie: " + str(round(promedio_s, 2)))
    print("Cantidad de países por continente:")
    for cont in por_cont:
        print("- " + cont + ": " + str(por_cont[cont]))


def mostrar_menu() -> None:                             #Muestra en pantalla el menú principal de opciones.    
    print("")
    print("***** Menú de Gestión de Países *****")
    print("")
    print("1. Agregar país")
    print("2. Actualizar país")
    print("3. Buscar país por nombre")
    print("4. Filtrar por continente")
    print("5. Filtrar por población")
    print("6. Filtrar por superficie")
    print("7. Ordenar países")
    print("8. Estadísticas")
    print("9. Guardar CSV")
    print("10. Mostrar todos los países")
    print("11. Salir")
    print("")


def main() -> None:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    ruta_csv = os.path.join(base_dir, "paises.csv")

    paises, errores = cargar_paises(ruta_csv)
    for e in errores:
        print("[AVISO]", e)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-11): ").strip()
        if not opcion.isdigit():
            print("Debe ingresar un número.")
            continue

        opcion = int(opcion)
        modificado = False

        if opcion == 1:
            modificado = agregar_pais(paises)
        elif opcion == 2:
            modificado = actualizar_pais(paises)
        elif opcion == 3:
            buscar_pais(paises)
        elif opcion == 4:
            filtrar_por_continente(paises)
        elif opcion == 5:
            filtrar_por_rango(paises, "poblacion", "Población")
        elif opcion == 6:
            filtrar_por_rango(paises, "superficie", "Superficie")
        elif opcion == 7:
            ordenar_paises(paises)
        elif opcion == 8:
            estadisticas(paises)
        elif opcion == 9:
            guardar_paises(ruta_csv, paises)
            print("Datos guardados correctamente.")
        elif opcion == 10:
            if len(paises) == 0:
                print("No hay países cargados.")
            else:
                for p in paises:
                    print("- " + p["nombre"] + ": población=" + str(p["poblacion"]) +
                          ", superficie=" + str(p["superficie"]) +
                          ", continente=" + p["continente"])
        elif opcion == 11:
            if len(paises) > 0:
                resp = input("¿Desea guardar antes de salir? (S/N): ").strip().upper()
                if resp == "S":
                    guardar_paises(ruta_csv, paises)
                    print("Datos guardados.")
            print("Saliendo del programa...")
            break
        else:
            print("Opción fuera de rango.")

        if modificado:
            guardar_paises(ruta_csv, paises)
            print("Cambios guardados automáticamente.")


if __name__ == "__main__":
    main()
