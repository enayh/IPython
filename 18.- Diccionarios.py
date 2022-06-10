# Diccionarios

diccionario = {}

diccionario_capitales = {'Chile' : 'Santiago', 'España' : 'Madrid', 'Argentina' : 'Buenos Aires'}

print(diccionario_capitales['España'])

for clave, valor in diccionario_capitales.items():
    print(valor)

print(diccionario_capitales.items()) # Retorna todos los items del diccionario [clave:valor]

print(diccionario_capitales.keys()) # Retorna todas las keys del diccionario

print(diccionario_capitales.values()) # Retorna todos los values del diccionario

print(len(diccionario_capitales)) # Largo del diccionario

print(type(diccionario_capitales)) # Tipo de dato

del diccionario_capitales['Chile'] # Elimina la key Chile y su value Santiago

"""
clear()	-> Removes all the elements from the dictionary
copy() -> Returns a copy of the dictionary
fromkeys() ->Returns a dictionary with the specified keys and value
get() -> Returns the value of the specified key
items()	-> Returns a list containing a tuple for each key value pair
keys() -> Returns a list containing the dictionary's keys
pop() -> Removes the element with the specified key
popitem() -> Removes the last inserted key-value pair
setdefault() -> Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update() -> Updates the dictionary with the specified key-value pairs
values() -> Returns a list of all the values in the dictionary

"""