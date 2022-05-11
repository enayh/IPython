# Funciones

#print("Mensaje de bienvenida")
#print("Aprendiendo Python")
#print("Mensaje de bienvenida")
#print("Aprendiendo Python")
#print("Mensaje de bienvenida")
#print("Aprendiendo Python")

def imprimir_mensaje():
    print("Mensaje de bienvenida")
    print("Aprendiendo Python")

imprimir_mensaje()
imprimir_mensaje()
imprimir_mensaje()

#Parametros

def saludo(nombre, apellido):
    print("Hola "+nombre+" "+apellido)

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
saludo(nombre, apellido)