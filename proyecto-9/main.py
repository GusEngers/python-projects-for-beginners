if __name__ == "__main__":
    class TicTacToe:
        def __init__(self):
            self.table_game = {
                "1": "1",
                "2": "2",
                "3": "3",
                "4": "4",
                "5": "5",
                "6": "6",
                "7": "7",
                "8": "8",
                "9": "9",
            }
            self.finish = False
            self.tie = False
        
        def _valid_move(self, move):
            if self.table_game[move].isdigit():
                return True
            return False
        
        def _is_win(self):
            if (self.table_game["1"] == "X" and self.table_game["2"] == "X" and self.table_game["3"] == "X") or (self.table_game["1"] == "O" and self.table_game["2"] == "O" and self.table_game["3"] == "O"):
                self.finish = True
                return True
            elif (self.table_game["4"] == "X" and self.table_game["5"] == "X" and self.table_game["6"] == "X") or (self.table_game["4"] == "O" and self.table_game["5"] == "O" and self.table_game["6"] == "O"):
                self.finish = True
                return True
            elif (self.table_game["7"] == "X" and self.table_game["8"] == "X" and self.table_game["9"] == "X") or (self.table_game["7"] == "O" and self.table_game["8"] == "O" and self.table_game["9"] == "O"):
                self.finish = True
                return True
            elif (self.table_game["1"] == "X" and self.table_game["4"] == "X" and self.table_game["7"] == "X") or (self.table_game["1"] == "O" and self.table_game["4"] == "O" and self.table_game["7"] == "O"):
                self.finish = True
                return True
            elif (self.table_game["2"] == "X" and self.table_game["5"] == "X" and self.table_game["8"] == "X") or (self.table_game["2"] == "O" and self.table_game["5"] == "O" and self.table_game["8"] == "O"):
                self.finish = True
                return True
            elif (self.table_game["3"] == "X" and self.table_game["6"] == "X" and self.table_game["9"] == "X") or (self.table_game["3"] == "O" and self.table_game["6"] == "O" and self.table_game["9"] == "O"):
                self.finish = True
                return True
            elif (self.table_game["1"] == "X" and self.table_game["5"] == "X" and self.table_game["9"] == "X") or (self.table_game["1"] == "O" and self.table_game["5"] == "O" and self.table_game["9"] == "O"):
                self.finish = True
                return True
            elif (self.table_game["3"] == "X" and self.table_game["5"] == "X" and self.table_game["7"] == "X") or (self.table_game["3"] == "O" and self.table_game["5"] == "O" and self.table_game["7"] == "O"):
                self.finish = True
                return True
            else:
                return False
        
        def _is_tie(self):
            values = 0
            for key in self.table_game:
                if not self.table_game[key].isdigit():
                  values += 1
            if values == 9:
                self.finish = True
                self.tie = True
                return True
            return False
        
        def move_player(self, player, move):
            if not self._valid_move(move):
                return "Movimiento no válido!"
            
            self.table_game[move] = player
            if self._is_win():
                return "Juego terminado!"
            if self._is_tie():
                return "Juego terminado!"
        
        def view_table(self):
            return f"""
              {self.table_game["1"]} | {self.table_game["2"]} | {self.table_game["3"]}
            -------------
              {self.table_game["4"]} | {self.table_game["5"]} | {self.table_game["6"]} 
            -------------
              {self.table_game["7"]} | {self.table_game["8"]} | {self.table_game["9"]}
            """
        
    game = TicTacToe()
    player_one = "X"
    player_two = "O"
    player_turn = 1

    print("***** BIENVENIDOS A 'TIC-TAC-TOE GAME' *****")

    while not game.finish:
        print(f"Turno del jugador {player_turn}")
        move = input("Elige la posición a mover: ")

        while not move.isdigit() or int(move) > 9:
            move = input("Por favor elige un movimiento válido: ")
        
        player = player_one if player_turn == 1 else player_two
        status_move = game.move_player(player, move)

        while status_move == "Movimiento no válido!":
            print(status_move)
            move = input("Por favor elige un movimiento válido: ")
            status_move = game.move_player(player, move)
        
        player_turn = 2 if player_turn == 1 else 1
        print(game.view_table())

    if game.tie:
        print("El juego termina en empate!")
    else:
        print(f"Gana el jugador {1 if player_turn == 2 else 2}!! FELICIDADES!!")
    
    print("********************************************")