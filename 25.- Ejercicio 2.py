# Escribir un programa que lea un archivo del "Ejercicio 1.py" y agregue cada linea a una lista y luego imprima la lista.

def main():
    lista = []
    with open('./archivos/tabla-4.txt', 'r') as file:
        for linea in file:
            lista.append(linea)
    print(lista)

if __name__ == '__main__':
    main()