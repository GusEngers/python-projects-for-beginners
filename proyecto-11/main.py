import random
import time

# Búsqueda nativa
# Una búsqueda normal iterando sobre todos los elementos hasta encontrar el valor
def native_search(lst, search):
    for i in range(len(lst)):
        if lst[i] == search:
            return i
    return -1

# Búsqueda binaria (sólo para listas ordenadas)
# Divide la búsqueda en partes hasta encontrar el valor
def binary_search(lst, search, _low=None, _high=None):
    if _low is None: # Si no se indica el índice mínimo, se asignará 0
        _low = 0
    if _high is None: # Si no se indica el índice máximo, se asignará el índice máximo de la lista
        _high = len(lst) - 1
    if _high < _low: # Si el índice máximo llega ser menor al mínimo significa que no ha encontrado el resultado
        return -1
    
    midpoint = (_low + _high) // 2 # Punto medio donde se dividirá la lista en dos
    
    if lst[midpoint] == search: # Si el valor que buscamos está en el punto medio retornaremos ese index
        return midpoint
    elif search < lst[midpoint]: # Si el valor que buscamos es menor al alojado en midpoint, volveremos a ejecutar
        return binary_search(lst, search, _low, midpoint - 1) # la función pero usando la primera parte de la lista
    else: # Caso contrario, retornaremos la función pero usando la segunda parte de la lista
        return binary_search(lst, search, midpoint + 1, _high)

# ************** Pruebas de tiempo *******************
# La diferencia de tiempo de búsqueda en listas grandes demuestra que la búsqueda binaria es muy superior
length = 10000
lst = set()

while len(lst) < length:
    lst.add(random.randint(-3 * length, 3 * length))
lst = sorted(list(lst))

start = time.time()
for search in lst:
    native_search(lst, search)
end = time.time()
print(f"Tiempo de búsqueda nativa: {round(end - start, 2)} seg.")

start = time.time()
for search in lst:
    binary_search(lst, search)
end = time.time()
print(f"Tiempo de búsqueda binaria: {round(end - start, 2)} seg.")