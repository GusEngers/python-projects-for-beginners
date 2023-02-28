# Ejercicio en el cual la computadora tendrá que adivinar
# el número que estamos pensando (dentro de un rango de números)
# a través de preguntas que nos irá haciendo,
# usando el módulo random

import random

if __name__ == "__main__":
    max_number = int(input("Ingrese el rango máximo (mayor a 1) que desee usar: "))
    min_number = 1
    feedback = ""

    while max_number <= 1:
        max_number = int(input("El rango máximo debe ser mayor a 1. Ingrese el rango máximo: "))

    print(f"Piensa en un número entre 1 y {max_number}")
    print("Responde con:\n → 'A' si el  número es más alto al que pensaste\n → 'B' si es más bajo al que pensaste\n → 'C' si es el número que pensaste")
    while feedback != "C":
        guess = random.randint(min_number, max_number)
        feedback = input(f"{guess} es el número que pensaste? ").upper()
        
        if feedback == "A":
            max_number = guess - 1
        if feedback == "B":
            min_number = guess + 1
            
    print("Si, he acertado el número!!")