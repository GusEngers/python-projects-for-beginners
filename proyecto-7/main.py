# Convertir texto en código QR usando el módulo qrcode, adémas de los módulos os (para
# obtener el path de la ruta) y uuid (para generar los nombres de las imágenes creadas).
# Tambien se puede ingresar la version de QR que quiera, todas las imágenes resultantes
# estarán dentro de la carpeta "images", así también el módulo qrcode está instalado
# dentro de un entorno virtual con pipenv.
# Queda pendiente la decodificación de la imagen!!

import qrcode
from os import getcwd
from uuid import uuid4

if __name__ == "__main__":
    data = input("Ingrese el texto a convertir en QR: ")
    while len(data) == 0:
        data = input("Por favor ingrese el texto: ")

    version = input("Elige la version de código QR entre el 1 y 40 (siendo 1 el más chico): ")
    while len(version) == 0 or version.isdigit() == False:
        if len(version):
            version = input("Por favor elige una versión: ")
        if version.isdigit() == False:
            version = input("La version tiene que ser un número menor o igual a 40: ")

    qr = qrcode.QRCode(version=int(version))
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image()
    img.save(f"{getcwd()}/images/{uuid4()}.png")
    print("Código QR creado!")