# Escriba una función que aleatoriamente escoja un número entero entre 1 y 10 y lo guarde en un fichero de nombre tabla-n.txt. Donde n es el número que salió. Escribir en el archivo la tabla del número.

import random

def numero_random():
    nr = random.randint(1, 10)

    with open('./archivos/tabla-'+str(nr)+'.txt', 'w', encoding="utf-8") as file:

        for multiplo in range(1, 13):
            file.write((str(nr)+(" * ")+str(multiplo)+(" = ")+str(nr * multiplo)))
            file.write("\n")

def main():
    numero_random()
    print("Archivo creado correctamente.")

if __name__ == '__main__':
    main()