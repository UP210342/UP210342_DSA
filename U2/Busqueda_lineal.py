lista_1 = [-5,2,3,6,1,9,14]
value_1 = 7
lista_2= [-3,0,5,7,9,10]
value_2 = 5
pos = 0


def LinealNotSort(lista_1):
    pos = 0
    for pos in range(len(lista_1)):
        if lista_1[pos] == value_1: 
            return pos
        elif pos == len(lista_1)-1:
            return False
    pos += 1

if LinealNotSort(lista_1) == False:
    print ('Valor no encontrado')
else:
     print('La posicion es: ',LinealNotSort(lista_1)) 

def LinealSort(lista_2):
    pos = 0
    for pos in range(len(lista_1)):
        if lista_2[pos] == value_2: 
            return pos
        elif lista_2[pos+1] > value_2:
            return False
    pos += 1

if LinealSort(lista_2) == False:
    print ('Valor no encontrado')
else:
     print('La posicion es: ',LinealSort(lista_2)) 