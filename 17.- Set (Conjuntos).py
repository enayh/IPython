# Sets (VALORES ÚNICOS) Desde Python 3.7 en adelante los sets están ordenados.

conjunto_vacio = set() # Así se define un diccionario vacío

conjunto = {0, 3, 4, 9, 5, 6} # Se puede definir un conjunto directamente

conjunto.add(1) # Agrega el elemento 1 al conjunto

conjunto_2 = {34, "mango", False}

conjunto.update(conjunto_2) # Agrega los valores del conjunto 2 al conjunto 1

print(conjunto)

conjunto_3 = conjunto.union(conjunto_2) # Los elementos del conjunto 3 será la unión del conjunto con el conjunto 2

repetidos = conjunto.intersection(conjunto_2) # Retorna los elementos repetidos entre el conjunto y el conjunto 2

lista = [1,1,1,2,2,2,3,3,3]

print(set(lista)) # Podemos transformar una lista a conjunto

print(len(conjunto)) # Largo del conjunto

print(type(conjunto)) # Tipo de dato

print(3 in conjunto) # Podemos saber si el elemento 3 está o no en el conjunto

conjunto.remove("mango") # Remueve el elemento mango del conjunto, si el elemento no se encuentra en el conjunto el programa arrojará un error.

conjunto.discard("hola") # Remueve el elemento hola del conjunto, si el elemento no se encuentra en el conjunto el programa NO arrojará un error.

conjunto.pop() # Remueve el último elemento del conjunto

conjunto.clear() # Remueve todos los elementos del conjunto

del conjunto # Elimina el conjunto

"""
add() -> Adds an element to the set
clear()	-> Removes all the elements from the set
copy() -> Returns a copy of the set
difference() -> Returns a set containing the difference between two or more sets
difference_update()	-> Removes the items in this set that are also included in another, specified set
discard() -> Remove the specified item
intersection() -> Returns a set, that is the intersection of two other sets
intersection_update() -> Removes the items in this set that are not present in other, specified set(s)
isdisjoint() -> Returns whether two sets have a intersection or not
issubset() -> Returns whether another set contains this set or not
issuperset() -> Returns whether this set contains another set or not
pop() -> Removes an element from the set
remove() -> Removes the specified element
symmetric_difference() -> Returns a set with the symmetric differences of two sets
symmetric_difference_update() -> inserts the symmetric differences from this set and another
union() -> Return a set containing the union of sets
update() -> Update the set with the union of this set and others

"""