# Listas

lista = [1, 2, 3, 4, 5, 'Nicolas']
lista_2 = [6, 7, 8, 9, 10]
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

x = tuple(lista) # Convierte la lista en una tupla

del lista # Elimina la lista

del lista[0] # Elimina un elemento específico de la lista según el índice que se le da

lista.clear() # Limpia por completo la lista