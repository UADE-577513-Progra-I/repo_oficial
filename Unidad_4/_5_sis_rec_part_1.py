# Sistema de recomendación - Parte 1

# ********** Importar librerias ***************
import random

# ******** Declaración de CONSTANTES ********

# filas: estudiantes
ESTUDIANTES = ["Lorenzo", "Mariano", "Ignacio", "Agustin", "Tatiana"]

# columnas: canciones - autores
TEMAS = [
    "Dai Dai - Shakira",
    "Dynamite - BTS",
    "Positions - Ariana Grande",
    "DTMF - Bad Bunny",
    "Dont start now - Dua Lipe",
]

# Matriz de ratings según calificaciones de los estudiantes
# 0 representa un tema todavía no escuchado/calificado.
RATINGS = [
    [3, 5, 0, 0, 0],  # Lorenzo
    [0, 0, 0, 5, 2],  # Mariano
    [0, 0, 0, 3, 5],  #
    [3, 4, 0, 0, 0],  #
    [5, 0, 0, 2, 0]
]


# ******** Declaración de la función principal ********
def main():
    print("Matriz de Ratings (original)")
    # print(RATINGS)
    mostrar_matriz(RATINGS)

    predicciones_random = generar_predicciones_random(RATINGS)
    print("\nMatriz de predicciones random")
    # mostrar_matriz(predicciones_random)

    predicciones_popularidad = generar_predicciones_popularidad(RATINGS)
    print("\nMatriz de predicciones popularidad")
    # mostrar_matriz(predicciones_popularidad)


# ******** Declaración de funciones secundarias ********
# Función que muestra una matriz en consola
def mostrar_matriz(matriz):
    """Muestra una matriz fila por fila.
    Argumento: matriz
    Returno Null
    """
    for i, fila in enumerate(matriz):
        print(f"i: {i} : fila: {fila}")


# Función que genera una matriz de predicciones random
def generar_predicciones_random(ratings):
    """
    Genera una matriz de predicciones del mismo tamaño que la matriz original.

    Para cada tema no escuchado (valor 0), genera un score aleatorio entre 1 y 5.
    Para los temas ya calificados, coloca 0 porque no necesitan predicción.
    """


# Función que genera una matriz nula (ceros)
def generar_matriz_nula(n_filas, n_columnas):
    """
    Genera una matriz de n x m dimensiones con 0 en todos sus valores
    Recibe como argumento n_fias, n_columnas
    Retorna la matriz nula
    """


# Función que traspone una matriz dada
def trasponer(matriz):
    """
    Genera una matriz traspuesta.
    Recibe una matriz de dimensión n x m
    Retorna su traspuesta de dimensión m x n
    """


# Función que calcula el rating promedio de cada tema
def calcular_ratings_avg(matriz):
    """
    Genera una lista cuyos elementos corresponden a los ratings promedio
    de cada tema. El rating promedio se calcula con las calificaciones
    de cada estudiante.

    Recibe como argumento una matriz
    Retorna una lista cuya longitud coincide con el número de columnas
    de la matriz
    """


# Función que genera una matriz de predicciones por popularidad
def generar_predicciones_popularidad(ratings):
    """
    Genera una matriz de predicciones del mismo tamaño que la matriz original.

    Para cada tema no escuchado (valor 0), genera un score con el rating promedio.
    Para los temas ya calificados, coloca 0 porque no necesitan predicción.
    """


# ******** Llamada función principal ********
if __name__ == "__main__":
    main()
