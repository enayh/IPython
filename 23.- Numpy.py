# Numpy

# Es una librería para el cálculo numérico y manejo de arreglos.
# Es más velóz y eficiente para manejar listas/arreglos en Python.
# Agrega soporte para grandes arreglos, multidimencionales y matrices.
# Es utilizada en el mundo de la IA y la ciencia de datos.

# Instalación
# En consola -> pip install numpy

# Importar
# import numpy as np

import numpy as np

def main():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(lista)
    print(type(lista))

    # Crear un array con numpy
    arreglo = np.array(lista)
    print(arreglo)
    print(type(arreglo))

    # Crear un array de 2 dimensiones
    matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(matriz)

    # Indexación de array
    print(arreglo[0]) # Retorna el elemento del índice 0 en el arreglo
    print(arreglo[0] + arreglo[1]) # Retorna el resultado del elemento del índice 0 + el elemento del índice 1

    # Indexación de matrices
    print(matriz[0]) # Retorna la primera fila
    print(matriz[0,0]) # Retorna el elemento que se encuentra en la posición (0,0)
    print(matriz[0,0] + matriz[0,1]) # Retorna el resultado del elemento en (0,0) + el elemento en (0,1)
    print(matriz[0:3])

if __name__  == '__main__':
    main()