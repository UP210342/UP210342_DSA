a = 5
b = a
print(b)
a = 6
print(b)

#no copia los valores, solo la direccion
list_1 = [3,5]
list_2 = list_1
print(list_2)
list_1[0] = 10
print('-->', list_2)

list_1 = [3,5,9,0]
list_2 = list_1[:]
list_1[0] = 10
print(list_2)
print('Lista --->')
print(list_1)
print(list_1[2:4]) # no toca el rango final
print(list_1[:])
print(list_1[0: len(list_1)])
print(list_1[1:-1])
print(list_1[1:])
print(list_1[:3])

del list_1[1:3]
del list_1[:]
