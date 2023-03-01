# Una cuenta regresiva usando el módulo time y un bucle while, empleando también el método divmod
# que devuelve dos resultados de una división (cociente y resto), formateo de números para que siempre
# tengan 2 dígitos (01 en vez de 1) como así tambien el caracter especial de retorno de carro para
# que no se llene la consola con texto en cada iteración, el método sleep de time para
# que la ejecución del código siga después de 1 segundo

import time

if __name__ == "__main__":
    def countdown(sec):
        while sec:
          minutes, seconds = divmod(sec, 60)
          timer = f"{minutes:02d}:{seconds:02d}"
          print(timer, end="\r")

          time.sleep(1)
          sec = sec - 1
        
        print("La cuenta regresiva ha terminado!")

    sec = int(input("Ingrese el tiempo en segundos: "))
    countdown(sec)