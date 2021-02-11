from socket import socket

def main():
    s = socket()
    s.connect(("localhost", 6030))

    while True:
        f = open("archivo.png", "rb")
        content = f.read(1024)

        while content:
            # Se manda el contenido
            s.send(content)
            content = f.read(1024)

        break
    # Se utiliza el caracter de codigo 1 para indicar
    # al cliente que ya se ha enviado todo el contenido.
    try:
        s.send(chr(1))
    except TypeError:
        # Compatibilidad con Python 3.
        s.send(bytes(chr(1), "utf-8"))

    # Cerrar conexion y archivo.
    s.close()
    f.close()
    print("El archivo ha sido enviado correctamente.")


if __name__ == "__main__":
    main()