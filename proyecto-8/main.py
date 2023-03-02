# Generador de contraseñas random usando una cantidad de contraseñas a generar y la longitud de las
# mismas, usando los módulos random (elección random de caracteres) y string (para obtener los 
# caracteres a usar). Se empleo tambien condicionales y bucles while y for para genererar las 
# contraseñas y verificar que los datos ingresados por el usuario cumplieran las condiciones.

import random
import string

if __name__ == "__main__":
    chars = string.ascii_letters + string.punctuation + "0123456789"
    
    print("***** Bienvenido al Generador de Contraseñas *****\n")

    number_passwords = input("Cuántas contraseñas quieres generar (mínimo 1): ")
    while not number_passwords.isdigit() or int(number_passwords) < 1:
        number_passwords = input("Por favor ingrese un número válido de contraseñas a generar: ")
    number_passwords = int(number_passwords)

    length_password = input("Cuál es la longitud de las contraseñas (mínimo 6): ")
    while not length_password.isdigit() or int(length_password) < 6:
        length_password = input("Por favor ingrese una longitud válida de contraseñas: ")
    length_password = int(length_password)

    print("Sus contraseñas son:\n")
    while number_passwords != 0:
        password = ""
        for c in range(int(length_password)):
            password += random.choice(chars)
        print(password)
        number_passwords -= 1
    
    print("\n***** Gracias por usar la aplicaión *****")