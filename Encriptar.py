# Encriptación
# Path: C:\Users\aniav\Downloads\Gato.jpg
# Key: 70

try:
    # Path de la imagen
    path = input('Ingresa la ruta de la imagen: ')

    # Llave de encriptación
    key = 70

    # Abrir el archivo
    archivo = open(path, 'rb')

    imagen = archivo.read()
    archivo.close()

    # Encriptación
    imagen = bytearray(imagen)

    # Operación XOR
    for indice, valores in enumerate(imagen):
        imagen[indice] = valores ^ key

    # Abrir archivo para escribir encriptación
    archivo = open(path, 'wb')
    archivo.write(imagen)
    archivo.close()
    print("Imagen Encriptada")

except Exception:
    print("Error: ", Exception.__name__)


# Desencriptación
# Para desencriptar la imagen se necesita ingresar la misma llave como clave

# try:
#     # Ingresar ruta de la imagen a desencriptar
#     path = input('Ingresa la ruta de la imagen: ')

#     key = 70

#     # Abrir el archivo para leer
#     archivo = open(path, 'rb')
#     imagen = archivo.read()
#     archivo.close()

#     # Desencriptación
#     imagen = bytearray(imagen)

#     # Operación XOR
#     for indice, valores in enumerate(imagen):
#         imagen[indice] = valores ^ key

#     # Abrir archivo para escribir desencriptación
#     archivo = open(path, 'wb')
#     archivo.write(imagen)
#     archivo.close()
#     print("Imagen Desencriptada")

# except Exception:
#     print("Error: ", Exception.__name__)