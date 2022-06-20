

import random

def ordenamiento_merge(lista):
    mid = len(lista) // 2
    if len(lista) > 1:
        l = lista[:mid]
        r = lista[mid:]

        lista.clear() #Limpia la lista que se recibió. Queda sin elementos.

        #Llamada recursiva.

        ordenamiento_merge(l)
        ordenamiento_merge(r)

        

        while len(l) > 0 and len(r) > 0:
            if l[0] < r[0]:
                lista.append(l.pop(0)) #Inserta en lista el menor elemento y lo borra de la otra lista, sea r o l
            else: 
                lista.append(r.pop(0))

        while len(l) > 0:
            lista.append(l.pop(0))
        while len(r) > 0:
            lista.append(r.pop(0)) 

       
    return lista    


if __name__ == "__main__":
    tamano_de_lista = int(input('¿De qué tamaño quieres que sea la lista?: '))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]

    print(lista)
    print('-' * 20)
    
    lista_ordenada = ordenamiento_merge(lista)

    print(lista_ordenada)