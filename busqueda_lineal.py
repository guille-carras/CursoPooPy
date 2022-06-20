#Busqueda lineal

import random


def busqueda_lineal(list, goal):
    match = False

    for elemento in list:
        if elemento == goal:
            match = True
            break
    
    return match




if __name__ == '__main__':
    tamano_lista = int(input('De que tamaño será la lista?'))
    objetivo = int(input('Qué número quieres encontrar?'))

    lista = [random.randint(0, 100) for i in range(tamano_lista)]

    encontrado = busqueda_lineal(lista, objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')