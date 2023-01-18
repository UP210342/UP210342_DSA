import array as arr

print("Hola\nMundo"); print("python")
print("\\")
print("Hola", "Mundo", end = "... \n")             #default end = "\n" sep = " "
print("Hola", "Mundo", end = "\n", sep = "-")
print('ooo' *2)

print( 'sofi\'s book.')
print( '"sofi\'s book"')

a = ('hola')
b = ('sksks')

print (a + b, sep = " "); print(b + a, end = '... \n')
print ('\n')

a = arr.array('i', [5,2,3])
print(a)
print(a[0])

b = [55,'69',420]
print(b)

b.append('jeje') #agrega al arreglo 
print(b)

b.pop(0) #borra al arreglo
print(b)