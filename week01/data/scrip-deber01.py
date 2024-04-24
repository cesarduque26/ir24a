import os

# Función para buscar una palabra en un archivo de texto
def buscar_palabra_en_archivo(archivo, palabra):
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            contenido = f.read()
            palabras_en_archivo = contenido.split()
            if palabra.lower() in palabras_en_archivo:
                return True
    except Exception as e:
        print(f"Error al leer el archivo {archivo}: {e}")
    return False

# Función para buscar una palabra en todos los libros
def buscar_palabra_en_libros(palabra):
    libros_con_palabra = []
    libros_directorio = os.listdir('.')
    for libro in libros_directorio:
        if libro.endswith(".txt"):
            if buscar_palabra_en_archivo(libro, palabra):
                libros_con_palabra.append(libro)
                print(f"La palabra '{palabra}' se encontró en el libro: {libro}")
    if not libros_con_palabra:
        print(f"No se encontró la palabra '{palabra}' en ninguno de los libros.")

# Bucle principal
while True:
    # Pedir al usuario la palabra a buscar
    palabra_buscar = input("Ingrese la palabra que desea buscar en los libros (o 'salir' para salir): ")
    
    # Salir del bucle si el usuario ingresa 'salir'
    if palabra_buscar.lower() == 'salir':
        print("Saliendo del programa...")
        break

    # Buscar la palabra en los libros
    buscar_palabra_en_libros(palabra_buscar)
