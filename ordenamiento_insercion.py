import random
from turtle import pos


def ordenamiento_por_incersion(lista):
    
    print(lista)
    for indice in range(1, len(lista)):
        valor_actual = lista[indice]
        posicion_actual = indice

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual = posicion_actual - 1

        lista[posicion_actual] = valor_actual
    
    print(lista)

def main():
    nums = [random.randint(1, 100) for i in range(1,100)]
    ordenamiento_por_incersion(nums)

if __name__ == '__main__':
    main()