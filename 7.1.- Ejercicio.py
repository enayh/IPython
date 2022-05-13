#Crear una calculadora básica (+, -, *, /) que opere dos números

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

operacion = input("Ingrese la operación que desea hacer (+, -, *, /): ")
if(operacion == "+"):
    a = int(input("Ingrese el primer número de la operación: "))
    b = int(input("Ingrese el segundo número de la operación: "))
    resultado = suma(a, b)
    print("El resultado de "+str(a)+" + "+str(b)+" es "+str(resultado))
elif(operacion == "-"):
    a = int(input("Ingrese el primer número de la operación: "))
    b = int(input("Ingrese el segundo número de la operación: "))
    resultado = resta(a, b)
    print("El resultado de "+str(a)+" - "+str(b)+" es "+str(resultado))
elif(operacion == "*"):
    a = int(input("Ingrese el primer número de la operación: "))
    b = int(input("Ingrese el segundo número de la operación: "))
    resultado = multiplicacion(a, b)
    print("El resultado de "+str(a)+" * "+str(b)+" es "+str(resultado))
elif(operacion == "/"):
    a = int(input("Ingrese el primer número de la operación: "))
    b = int(input("Ingrese el segundo número de la operación: "))
    resultado = division(a, b)
    print("El resultado de "+str(a)+" / "+str(b)+" es "+str(resultado))
else:
    print("Ingrese un caracter válido.")
