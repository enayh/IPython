# Tarea 1
# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

peso_payaso = 112
peso_muneca = 75

cantidad_payasos = int(input("Ingrese la cantidad de payasos que hay en el paquete: "))
cantidad_munecas = int(input("Ingrese la cantidad de muñecas que hay en el paquete: "))
#if (cantidad_payasos or cantidad_munecas) < 0:
if cantidad_payasos < 0 or cantidad_munecas < 0:
    print("Ingrese un valor válido.")
#elif (cantidad_payasos and cantidad_munecas) == 0:
elif cantidad_payasos == 0 and cantidad_munecas == 0:
    print("No se ha vendido nada.")
else:
    peso1 = peso_payaso * cantidad_payasos
    peso2 = cantidad_munecas * peso_muneca
    peso_total = peso1 + peso2

    cantidad_payasos = str(cantidad_payasos)
    cantidad_munecas = str(cantidad_munecas)
    peso_total = str(peso_total)

    print("La cantidad de payasos y muñecas vendidos en el último pedido fueron de "+cantidad_payasos+" Payaso(s) y "+cantidad_munecas+" Muñeca(s)")
    print("El peso total del paquete es de "+peso_total+"g")


# Tarea 2
# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, e imprima por pantalla la frase "Tu índice de masa corporal es <imc>" donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

peso = float(input("Ingrese su peso(kg): "))
estatura = float(input("Ingrese su estatura(m): "))
imc = peso/estatura**2
imc = round(imc, 2)
imc = str(imc)
print("Tu índice de masa corporal es "+imc)
