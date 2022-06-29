# Manejo de archivos

# with -> Si el programa se cierra inesperadamente, evita que se corrompa el archivo. (Manejador contextual)
# r -> Sólo lectura.
# r+ -> Lectura y escritura.
# w -> Sólo escritura. Sobreescribe el archivo si exíste, sino lo crea.
# w+ -> Escritura y lectura. Sobreescribe el archivo si exíste, sino lo crea.
# a -> Añadido. Crea el archivo si no existe
# a+ Añadido y lectura. Crea el archivo si no existe

def leer():
    numeros = []
    with open('./archivos/numeros.txt', 'r') as file:
        for linea in file:
            numeros.append( int(linea) )
    
    print( numeros )

def escribir():
    nombres = ['Ezequiel', 'Juan', 'Rocío', 'David']
    with open('./archivos/nombres.txt', 'w', encoding="utf-8") as file:
        for nombre in nombres:
            file.write(nombre)
            file.write("\n")

def main():
    escribir()

if __name__ == '__main__':
    main()