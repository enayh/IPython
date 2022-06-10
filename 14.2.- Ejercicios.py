# Ejercicio 3: Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 12. El usuario debe ingresar el número.

def main():
    numero = int(input("Ingrese un número: "))
    for multiplo in range(1, 13):
        print(str(numero)+(" * ")+str(multiplo)+(" = ")+str(numero * multiplo))
    
if __name__ == '__main__':
    main()