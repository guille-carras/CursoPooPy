import random


def ordenamiento_burbuja(lista):
    n = len(lista)

    for i in range(n):

        for j in range(0, n - i - 1):

            if lista[j] > lista[j + 1]:
                lista[j + 1], lista[j] = lista[j], lista[j + 1]
    
    return lista    
            
if __name__ == '__main__':
    
    lista = [random.randint(0, 100) for i in range(0, 100)]

    new_list = ordenamiento_burbuja(lista)

    print(new_list)  