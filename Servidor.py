from socket import socket, error
from names.words import GetName

def main():
    print("El servidor está listo")

    # Este ciclo mantiene al servidor corriendo indefinidamente, esperando nuevas conexiones hasta que se detenga manualmente
    while True:
        s = socket()

        s.bind(("localhost", 6030))
        s.listen(0)

        # Crea un socket (conn) que acepta nuevas conexiones. Se mantiene esperando hasta que se reciba una conexión
        conn, addr = s.accept()
        f = open(f"ImagenesRecibidas\\{GetName()}.jpg", "wb")
        print(f'Conexión de {addr[0]}:{addr[1]}')

        while True:
            # Después de recibir una conexión, se leen los datos almacenados en el buffer del socket
            data = conn.recv(1024)
            # Cuando el buffer se vacia, se cierra el archivo y se sale del ciclo.
            # El cierre de la conexión se realiza del lado del cliente
            if not data:
                print("Imagen guardada")    
                f.close()
                break
            else:
                f.write(data) 
        

if __name__ == "__main__":
    main()