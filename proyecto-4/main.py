# Simple juego de piedra, papel o tijeras del usuario contra la computadora,
# usando el módulo random junto con su método choice, además de condicionales
# if's y while's

import random

if __name__ == "__main__":
    print("""Las reglas son:
    → Debes indicar la cantidad de rondas a jugar
    → Debes elegir 'r' para Piedra, 'p' para Papel, 's' para Tijeras
    → Piedra gana Tijeras
    → Papel gana Piedra
    → Tijeras gana Papel
    → Ganar suma 1 punto
    → Perder o empatar no suma puntos""")

    rounds = int(input("Cuantas rondas quieres jugar? "))
    comp_win = 0
    user_win = 0

    def is_win(user, opponent):
        """
        Recibe dos argumentos y los compara, devolviendo True si el usuario gana y False si la
        computadora gana, además de modificar las variables globales comp_win y user_win
        
        :user - Sus posibles valores son "r", "p", "s"
        :opponent - Sus posibles valores son "r", "p", "s"
        """
        if (user == "r" and opponent == "s") or (user == "p" and opponent == "r") or (user == "s" and opponent == "p"):
            globals()["user_win"] = globals()["user_win"] + 1
            return True
        else:
            globals()["comp_win"] = globals()["comp_win"] + 1
            return False
    
    def what_choise(arg):
        """
        Recibe un caracter del juego y devuelve su significado ("Piedra", "Papel" o "Tijeras")

        :arg - Sus posibles valores son "r", "p", "s"
        """
        if arg == "r":
            return "Piedra"
        elif arg == "p":
            return "Papel"
        else:
            return "Tijeras"
    
    def play():
        """
        Función principal del juego donde recibiremos por la consola un caracter específico
        y luego realizará las comparaciones repectivas y retornará el resultado del juego
        """
        user = input("Elige piedra, papel o tijeras: ").lower()
        while user != "r" and user != "p" and user != "s":
            user = input("Solo se aceptan los valores 'r', 'p' o 's': ").lower()
        
        comp = random.choice(["r", "p", "s"])

        if user == comp:
            return f"Han empatado!! Ambos eligieron {what_choise(user)}!!"
        elif is_win(user, comp):
            return f"Has ganado!! Elegiste {what_choise(user)} mientras que la computadora eligió {what_choise(comp)}!!"
        
        return f"Has perdido!! Elegiste {what_choise(user)} mientras que la computadora eligió {what_choise(comp)}!!"
    
    while rounds != 0:
        print(play())
        rounds = rounds - 1
    
    if user_win > comp_win:
        print(f"Has ganado la partida {user_win} a {comp_win}")
    elif user_win < comp_win:
        print(f"Has perdido la partida {comp_win} a {user_win}")
    elif user_win == comp_win:
        print(f"Han empatado la partida {user_win} a {comp_win}")
