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
    
        

a = [432,76579,324,56,3,1]
primero = 0
final  = len(a)-1

print(a)
Quicksort(a,primero,final)
print(a)

