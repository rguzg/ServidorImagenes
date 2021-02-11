from socket import socket, error

def main():
    s = socket()

    s.bind(("localhost", 6030))
    s.listen(0)

    print("El servidor esta listo")

    conn, addr = s.accept()
    f = open("recibido.png", "wb")

    while True:
        try:
            # Recibir datos del cliente.
            input_data = conn.recv(1024)
        except error:
            print("Error de lectura.")
            break
        else:
            if input_data:
                # Compatibilidad con Python 3.
                if isinstance(input_data, bytes):
                    end = input_data[0] == 1
                else:
                    end = input_data == chr(1)
                if not end:
                    # Almacenar datos.
                    f.write(input_data)
                else:
                    break
    f.close()


if __name__ == "__main__":
    main()