from socket import socket
from Encriptar import Encriptar
from ChecarImagenesFinal import ChecarImagen

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

    ChecarImagen.CompararImagen(ARCHIVO, 'resultado.png')

if __name__ == "__main__":
    main()