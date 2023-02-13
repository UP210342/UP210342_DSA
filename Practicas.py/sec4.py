m = (int ('5') + 5)
print(m)

keywords = [ 'True', 'False', 'None', 'True', 'and', 'as', 'assert', 'class']

print(keywords[4]) #busca el dato en el vector

print(keywords.index('True')) #busca la posicion en el vector

print(keywords.pop(), keywords.pop(), keywords.pop(1), keywords[1])

keywords.insert(2, 'ola') #agrega a la posicion que se quiera 
print(keywords)
print('Conteo: ', keywords.count('True')) #Cuenta el numero de veces que aparece un dato
print('Conteo: ', len(keywords)) #Contar el num de datos en total

x = 2
x+=1 #Shortcut operation
print(x)

print(round(3.14159,4)) #Redondear 

y = '5' + '2' #Concatenar 
print(y)

a = 6
b = 3 
a /= 2 * b
print(a) #1

