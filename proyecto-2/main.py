# Ejercicio en el cual tendremos que adivinar el número generado por random

import random

if __name__ == "__main__":
    def guess_computer():
        max_number = int(input("Ingrese el rango máximo (mayor a 1) que desee usar: "))
        while max_number <= 1:
            max_number = int(input("El rango máximo debe ser mayor a 1. Ingrese el rango máximo: "))
        
        random_number = random.randint(1, max_number)
        user_number = 0

        while user_number != random_number:
            user_number = int(input(f"Elige un número entre 1 y {max_number}: "))
            if user_number < random_number:
                print("El número a adivinar es más grande!")
            elif user_number > random_number:
                print("El número a adivinar es más chico!")
        
        print(f"Exacto! El número era {user_number}!!!")
    
    guess_computer()