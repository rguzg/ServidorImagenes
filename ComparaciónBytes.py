from typing import Any, List

# Compara byte por byte dos archivos y retorna sin son iguales o no
def ComparacionBytes(file_path1: str, file_path2: str) -> List:
    file = open(file_path1, 'rb')
    resultado =  open(file_path2, 'rb')

    iguales = True
    bytes_desiguales = []

    for byte, byteR in zip(file, resultado):
        if(byte != byteR):
            iguales = False
            bytes_desiguales.append((byte, byteR))

    return [iguales, bytes_desiguales]
