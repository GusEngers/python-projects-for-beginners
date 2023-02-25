# Ejercicio donde recibimos datos del usuario y lo mostramos en pantalla
# usando concatenación de strings

if __name__ == "__main__":

  print("Completa los siguientes campos")

  adj = input("Adjetivo: ")
  verb1 = input("Verbo conjugado: ")
  verb2 = input("Verbo conjugado: ")
  famous_person = input("Persona famosa: ")
  option_text = int(input("Elige un número del 1 al 3: "))

  if option_text == 1:
    print(f"{famous_person.title()} {verb1.lower()} un pastel mientras {verb2.lower()} un {adj.lower()} castillo.")
  elif option_text == 2:
    print(f"{verb1.capitalize()} sobre una carretera cuando {famous_person.title()} se {verb2.lower()} una {adj.lower()} montaña.")
  elif option_text == 3:
    print(f"Cuando {famous_person.title()} llega todas los {adj.lower()} regalos {verb1.lower()} y {verb2.lower()} una y otra vez.")
  else:
    print("Veo que no sigues las reglas... ELIGE UN NÚMERO CORRECTO!")