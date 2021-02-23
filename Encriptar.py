# Encriptación
# Path: C:\Users\aniav\Downloads\Gato.jpg
# Key: 70
def Encriptar(img):
    try:
        # Path de la imagen
        path = img

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

        print("Imagen Encriptada")
        return imagen

    except Exception:
        print("Error: ", Exception.__name__)


# Desencriptación
# Para desencriptar la imagen se necesita ingresar la misma llave como clave
def Desencriptar(byte):
    key = 70

    return int.from_bytes(byte, 'big') ^ key
