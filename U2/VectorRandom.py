import random

def NoRepetir(x,vector):
    NoR = True
    for pos in range(len(vector)):
        if x == vector[pos]:
            NoR = False
            break
    return NoR

def Quicksort(a, primero, ultimo):
    central = (primero + ultimo) // 2
    pivote = a[central]
    i = primero
    j = ultimo

    while i<=j:
        while a[i] < pivote:
            i+=1
        while a[j] > pivote:
            j-=1
        if i <= j:
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
            i+=1
            j-=1

    if primero < j:
        Quicksort(a,primero,j)
    if i < ultimo:
        Quicksort(a,i,ultimo)

    return a

def BinarySearch(datos,elemento):
    li = 0
    ls = len(datos)-1
    prin = li
    final = ls
    mit = int((prin + final)//2)
    con = 0

    while prin <= final and datos[mit] != elemento:
        if elemento < datos[mit]:
            final = mit - 1 #Lado izquierdo 
        else:
            prin = mit + 1 #Lado derecho
        mit = int((prin + final)//2)
        con += 1

    if datos[mit] == elemento:
        pos = mit
    else:
        pos = False
    
    return pos,con

vector = []
n = 0
inicio = 0
final = len(vector) -1

while n < 10:
  x = random.randint(101,500)
  if NoRepetir(x,vector):
    vector.append(x)
    n+=1

primero = 0
final = len(vector) -1

print('\nVector random sin organizar: ',vector)

Quicksort(vector,primero,final)
print('\nVector random organizado: ',vector)

elemento = int(input('\nIngresa el elemento que deseas buscar: '))
x,y = BinarySearch(vector,elemento)
print('\nLa posicion es: ',x,' y se busco ',y,' veces\n')