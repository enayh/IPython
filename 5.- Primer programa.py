# Transformar pesos chilenos a dólares
# El programa debe pedir una cantidad de CLP y mostrar el resultado en USD

clp = float(input("Ingrese la cantidad de CLP: "))
valor_usd = 857.08
usd = clp / valor_usd
usd = round(usd, 2)
usd = str(usd)
print("Usted tiene $USD " + usd)

# Tarea: programa que transforme USD a CLP

usd = float(input("Ingrese la cantidad de USD: "))
valor_usd = 857.08
clp = usd * valor_usd
clp = round(clp, 2)
clp = str(clp)
print("Usted tiene $CLP " + clp)
#AL REDONDEAR EL RESULTADO, LA CONVERSIÓN NO ES EXACTA