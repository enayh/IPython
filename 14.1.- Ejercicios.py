# Ejercicio 2: Escriba un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido desde 1 hasta su edad
def main():
    edad = int(input("Ingrese su edad: "))
    for annos in range(1, edad+1):
        print(annos)

if __name__ == '__main__':
    main()