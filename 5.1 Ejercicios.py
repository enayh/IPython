# Ejercicio 1
# Escribir un programa que pregunte el nombre por consola y un número entero e imprimir por pantalla el nombre tantas veces como el numero ingresado

nombre = input("Ingrese un nombre: ")
numero = int(input("Ingrese un numero: "))
print(nombre * numero)

# Ejercicio 2
# Escribir un programa que muestre por pantalla el resultado de la siguiente operación matemática

print(((3+2)/(2*5))**2)

# Ejercicio 3
# Escribir un programa que lea un entero positivo n introducido por el usuario y después muestre por pantalla la suma de todos los enteros desde 1 hasta n.

numero = int(input("Ingrese un numero positivo: "))
if numero >= 1:
    suma = (numero*(numero+1))/2
    suma = str(suma)
    numero = str(numero)
    print("La suma de los primeros numeros desde 1 hasta " + numero + " es de " + suma)
else:
    print("El numero no es mayor o igual a 1")