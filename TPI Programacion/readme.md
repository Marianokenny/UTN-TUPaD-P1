# Programa de Gestión de Países

## 🌍 Descripción
Este programa permite **administrar información de países** almacenada en un archivo CSV (`paises.csv`).  

Funciones principales:

- Agregar y actualizar países (nombre, población, superficie y continente).  
- Buscar países por nombre (coincidencia parcial).  
- Filtrar países por continente, población o superficie.  
- Ordenar la lista de países por nombre, población o superficie.  
- Mostrar estadísticas generales:  
  - País con mayor y menor población  
  - Promedios de población y superficie  
  - Cantidad de países por continente  
- Guardar y cargar datos automáticamente en CSV.  

El programa se ejecuta desde la **terminal** y cuenta con un **menú interactivo** de opciones.

## 💻 Instrucciones de uso

1. Clonar o descargar el repositorio.  
2. Asegurarse de tener **Python 3** instalado.  
3. Ubicar el archivo `paises.csv` en la misma carpeta que el script (opcional; si no existe, se creará uno nuevo).  
4. Ejecutar el programa 

## 💻 Ejemplo opción 1 Agregar país:

Seleccione una opción (1-11): 1
Nombre del país: Argentina
Población (entero): 45000000
Superficie en km² (entero): 2780000
Continente: América
País 'Argentina' agregado correctamente.
Cambios guardados automáticamente.

## 💻 Ejemplo opción 3 Buscar país:

Seleccione una opción (1-11): 3
Buscar por nombre: arg
- Argentina: población=45000000, superficie=2780000, continente=América

## 💻 Ejemplo opción 4 Filtrar por continente:

Seleccione una opción (1-11): 4
Ingrese continente: América
- Argentina: población=45000000, superficie=2780000
- Brasil: población=210000000, superficie=8516000

## 💻 Ejemplo opción 8 estadisticas:

Seleccione una opción (1-11): 8
País con mayor población: Brasil (210000000)
País con menor población: Argentina (45000000)
Promedio población: 127500000.0
Promedio superficie: 5648000.0
Cantidad de países por continente:
- América: 2
- Europa: 3

## 💻 Integrantes:

Mariano Kenny
Sebastián Kocuta
Comisión 7
Fecha: 11/11/2025


