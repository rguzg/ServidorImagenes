from socket import socket
from Encriptar import Encriptar
from ChecarImagenesFinal import ChecarImagen
from ComparaciónBytes import ComparacionBytes

ARCHIVO = "Gato.jpg"

def main():
    s = socket()
    s.connect(("localhost", 6030))

    # Encriptar imagen. Este método retorno un bytearray de la imagen encriptada
    archivo_encriptado = Encriptar(ARCHIVO)
    resultado = open('Resultado.png', 'wb')

    for byte in archivo_encriptado:
        # Se manda el contenido
        # Cada elemento de archivo_encriptado es un entero, así que se convierte el entero a bytes
        s.send(byte.to_bytes(1, 'big'))
        
        resultado.write(s.recv(1024))

    s.close()

    iguales, diferencias = ComparacionBytes(ARCHIVO, 'Resultado.png')

    if(iguales):
        print("Las imagenes son iguales")
    else:
        print("Las imagenes no son iguales")
        print("Diferencias: ")
        print(diferencias)
        

if __name__ == "__main__":
    main()