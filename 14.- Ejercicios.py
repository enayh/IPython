# Ejercicio 1: Escribir una función a la que se le pase una cadena <nombre> y muestre en pantalla el saludo Hola <nombre>

def main():
    nombre = input("Ingrese su nombre: ")
    nombre = nombre.capitalize()
    print("¡Hola "+nombre+("!"))

if __name__ == '__main__':
    main()