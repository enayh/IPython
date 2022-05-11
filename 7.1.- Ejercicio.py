#Crear una calculadora básica (+, -, *, /) que opere dos números

def suma(num1, num2, resultado):
    resultado = num1 + num2
    num1 = str(num1)
    num2 = str(num2)
    resultado = str(resultado)
    print("El resultado de "+num1+" + "+num2+" es "+resultado)

def resta(num1, num2, resultado):
    resultado = num1 - num2
    num1 = str(num1)
    num2 = str(num2)
    resultado = str(resultado)
    print("El resultado de "+num1+" - "+num2+" es "+resultado)

def multiplicacion(num1, num2, resultado):
    resultado = num1 * num2
    num1 = str(num1)
    num2 = str(num2)
    resultado = str(resultado)
    print("El resultado de "+num1+" * "+num2+" es "+resultado)

def division(num1, num2, resultado):
    resultado = num1 / num2
    resultado = round(resultado, 2)
    num1 = str(num1)
    num2 = str(num2)
    resultado = str(resultado)
    print("El resultado de "+num1+" / "+num2+" es "+resultado)

operacion = input("Ingrese la operación que desea hacer (+, -, *, /): ")

if(operacion == "+"):
    num1 = int(input("Ingrese el primer número de su operación: "))
    num2 = int(input("Ingrese el segundo número de su operación: "))
    resultado = ()
    suma(num1, num2, resultado)
elif(operacion == "-"):
    num1 = int(input("Ingrese el primer número de su operación: "))
    num2 = int(input("Ingrese el segundo número de su operación: "))
    resultado = ()
    resta(num1, num2, resultado)
elif(operacion == "*"):
    num1 = int(input("Ingrese el primer número de su operación: "))
    num2 = int(input("Ingrese el segundo número de su operación: "))
    resultado = ()
    multiplicacion(num1, num2, resultado)
elif(operacion == "/"):
    num1 = int(input("Ingrese el primer número de su operación: "))
    num2 = int(input("Ingrese el segundo número de su operación: "))
    resultado = ()
    division(num1, num2, resultado)
else:
    print("Ingrese un caracter válido.")