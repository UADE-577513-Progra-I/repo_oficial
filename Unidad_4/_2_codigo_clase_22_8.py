
matriz = [] # Declarar

fila0 = [1, 3, 2]
fila1 = [3, 5, 1]

# Inicializar
matriz = [fila0, fila1]

# Asigno las filas a la matriz
matriz.append(fila0)
matriz.append(fila1)

print(matriz[1][2])


# mostrar opcion1 - range - indice
for i in range(len(matriz)):
    print(matriz[i])

# mostrar opcion2 - valores
for fila in matriz:
    print(fila)

# mostrar opcion3 - enumerate (indice, valores)
for indice, fila in enumerate(matriz):
    print(f"Indice de fila: {indice} - Fila/valor: {fila}")

# Generar la matriz de manera dinamica
# Matriz nula - todos 0
# Dimension: 2 filas / 3 columnas
def gen_matriz_nula(nFilas, nColumnas):
    matriz_nula = []
    # nFilas = 2
    # nColumnas = 3
    for i in range(nFilas): # para las filas
        fila = []
        for j in range(nColumnas): # para las columnas
            fila.append(0)
        matriz_nula.append(fila)
    # print(matriz_nula)
    return matriz_nula

def gen_matriz_unos(nFilas, nColumnas):
    matriz_unos = []
    # nFilas = 2
    # nColumnas = 3
    for i in range(nFilas): # para las filas
        fila = []
        for j in range(nColumnas): # para las columnas
            fila.append(1) # <-- 1
        matriz_unos.append(fila)
    # print(matriz_nula)
    return matriz_unos

matriz_unos = gen_matriz_unos(nColumnas=3, nFilas=2) # por posicion / nombrados
print(matriz_unos)

import random
def gen_matriz_random(nFilas, nColumnas, min = 1, max = 5):
    matriz_random = []
    # nFilas = 2
    # nColumnas = 3
    for i in range(nFilas): # para las filas
        fila = []
        for j in range(nColumnas): # para las columnas
            fila.append(random.randint(min, max)) # <-- random.randint(1,5)
        matriz_random.append(fila)
    # print(matriz_nula)
    return matriz_random

matriz_random = gen_matriz_random(nColumnas=3, nFilas=2) # por posicion / nombrados
print(matriz_random)


def gen_matriz_identidad(nFilas, nColumnas):
    matriz_identidad = []
    # nFilas = 2
    # nColumnas = 3
    for i in range(nFilas): # para las filas
        fila = []
        for j in range(nColumnas): # para las columnas
            if i == j:
                fila.append(1)
            else:
                fila.append(0) # <-- if i == j pongo 1 else pongo 0
        matriz_identidad.append(fila)
    # print(matriz_nula)
    return matriz_identidad

matriz_identidad = gen_matriz_identidad(nColumnas=3, nFilas=3) # por posicion / nombrados
print(matriz_identidad)