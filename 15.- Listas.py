# Listas

lista = [1, 2, 3, 4, 5, 'Nicolas']

lista_2 = [6, 7, 8, 9, 10]

lista_3 = [3, 8, 1, 0, 5, 4]

print(lista)

print(len(lista)) # Largo de la lista

print(type(lista)) # Tipo de dato

print(lista[1]) # Acceder al elemento de índice 1

print(lista[-1]) # Acceder al último elemento de la lista

print(lista[2:5]) # Recorre desde el índice 2 hasta 5(-1)

print(lista[:5]) # Recorre desde el índice 0 hasta 5(-1)

print(lista[2:]) # Recorre desde el índice 2 hasta el final

if 1 in lista: # Si 1 se encuentra en la lista
    print("El 1 se encuentra en la lista")

lista[1] = "black" # Cambia el elemento que se encuentra en el índice 1 por "black"

lista[1:3] = ["black", "white"] # Cambia el elemento que se encuentra en el índice 1 por "black" y el elemento que se encuentra en el índice 3(-1) por "white"

lista.insert(2, "rose") # Inserta en el índice 2 el elementro "rose"

lista.append("orange") # Inserta al final de la lista el elemento "orange"

lista.extend(lista_2) # Agrega al final de lista los elementos de lista_2

lista.remove("Nicolas") # Remueve un elemento específico de la lista

lista.pop() # Remueve el último elemento de la lista

lista.pop(2) # Remueve un elemento específico de la lista según el índice que se le da

lista_3.sort() # Ordena la lista

x = tuple(lista) # Convierte la lista en una tupla

lista.clear() # Remueve todos los elementos de la lista

del lista # Elimina la lista

""" 
append() -> Adds an element at the end of the list
clear() -> Removes all the elements from the list
copy() -> Returns a copy of the list
count() -> Returns the number of elements with the specified value
extend() -> Add the elements of a list (or any iterable), to the end of the current list
index() -> Returns the index of the first element with the specified value
insert() -> Adds an element at the specified position
pop() -> Removes the element at the specified position
remove() -> Removes the item with the specified value
reverse() -> Reverses the order of the list
sort() -> Sorts the list

"""