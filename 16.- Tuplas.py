# Tuplas (INMUTABLES)

tupla = (1, 2 , 3, 4, 5, 6)

print(tupla)

print(len(tupla)) # Largo de la tupla

print(type(tupla)) # Tipo de dato

print(tupla[1]) # Acceder al elemento de índice 1

print(tupla[-1]) # Acceder al último elemento de la tupla

print(tupla[2:5]) # Recorre desde el índice 2 hasta 5(-1)

print(tupla[:5]) # Recorre desde el índice 0 hasta 5(-1)

print(tupla[2:]) # Recorre desde el índice 2 hasta el final

if 1 in tupla: # Si 1 se encuentra en la tupla
    print("El 1 se encuentra en la tupla")

print(tupla.count(3)) # Retorna el valor de las veces que aparece el 3, en este caso 1

print(tupla.index(3)) # Retorna el índice en donde se encuentra el 3, en este caso es 2

x = list(tupla) # Convierte la tupla en una lista

del tupla # Elimina la tupla