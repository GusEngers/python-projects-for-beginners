# Juego del ahorcado en la consola, usando el módulo random (para elegir una palabra random del módulo
# con la lista de palabras), el módulo string (para obtener el alfabeto), y módulos propios donde están
# la lista de palabras y el diccionario con la visual del personaje.
# Se emplearon tanto las estructuras set como diccionarios y listas, y controlando el flujo mediante
# condicionales if's y while's

import random
from words import words
import string
from lives_hangman import lives_hangman as HANGMAN

if __name__ == "__main__":
    def validate_word(words):
        word = random.choice(words)

        while " " in word or "-" in word:
            word = random.choice(words)

        return word.upper()

    def hangman():
      word = validate_word(words)
      word_letters = set(word)
      alphabet = set(string.ascii_uppercase)
      used_letters = set()
      lives = 7

      while len(word_letters) > 0 and lives > 0:
          print(f"Tienes {lives} vidas")
          print(HANGMAN[lives])
          user_letter = input("Ingresa una letra: ").upper()

          if user_letter in used_letters:
              print("Ya has usado esa letra, intenta con otra!")
          elif user_letter not in alphabet:
              print("El caracter ingresado no es una letra, prueba otra vez!")
          elif user_letter in alphabet and user_letter not in used_letters:
              used_letters.add(user_letter)
              if user_letter in word_letters:
                  word_letters.remove(user_letter)
                  print("Correcto")
              else:
                  lives = lives - 1
                  print(f"La letra {user_letter} no está en la palabra")
      
      if lives == 0:
          print(f"Has perdido! La palabra era '{word}'!")
      else:
          print(f"Has ganado! La palabra era '{word}'!")
    
    hangman()
      