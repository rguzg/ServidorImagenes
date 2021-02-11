from socket import socket, error

def main():
    while True:
        s = socket()

        s.bind(("localhost", 6030))
        s.listen(0)

        print("El servidor esta listo")

        conn, addr = s.accept()
        f = open("recibido.jpg", "wb")


# Cambiar esto por algo que tenga más forma: https://docs.python.org/3/library/socket.html#example
        while True:
            try:
                # Recibir datos del cliente.
                input_data = conn.recv(1024)
            except error:
                print("Error de lectura.")
                break

            if input_data:
                # Mover esto a otro lado para que el archivo no se corrompa (Implementar lo de nombres aleatorios?)
                # Compatibilidad con Python 3.
                if isinstance(input_data, bytes):
                    end = input_data[0] == 1
                else:
                    end = input_data == chr(1)
                if not end:
                    # Almacenar datos.
                    f.write(input_data)
                else:
                    print("Imagen guardada")
                    f.close()
                    break
            else:
                print("Imagen guardada")
                break


if __name__ == "__main__":
    main()