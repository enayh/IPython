# Break & Continue
def main():
    # Imprimir impares
    for contador in range(1, 100):
        if contador % 2 == 0:
            continue
        print(contador)
    
    for numero in range(100):
        print(numero)
        if numero == 8:
            break
    
    
    texto = input("Ingrese un texto:")
    for letra in texto:
        if letra == 'a':
            break
        print(letra)

if __name__ == '__main__':
    main()