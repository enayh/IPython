# Diccionarios

diccionario = {}

diccionario_capitales = {'Chile' : 'Santiago', 'España' : 'Madrid', 'Argentina' : 'Mendoza'}

print(diccionario_capitales['España'])

for clave, valor in diccionario_capitales.items():
    print(valor)

print(diccionario_capitales.items()) # Retorna todos los items del diccionario [clave:valor]

print(diccionario_capitales.keys()) # Retorna todas las keys del diccionario

print(diccionario_capitales.values()) # Retorna todos los values del diccionario

print(len(diccionario_capitales)) # Largo del diccionario

print(type(diccionario_capitales)) # Tipo de dato