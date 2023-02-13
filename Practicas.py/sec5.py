#FUNCION:
def ordenar(stack):
    return len(stack) == 0

def doble(x):
    y = x *2
    return y

#------------------------------#

a = [5,2,7,9,3]

#FOR: 
for i in range(0, len(a)):
    print(a[i])

#------------------------------#

#BUBBLE SORT:

for i in range(0, len(a) +1 -2):
    for j in range(0, len(a) +1 - i-2):
        x = a[j]
        y = a[j+1]
        if x > y:
            a[j] = y
            a[j+1] = x

print(a)

#------------------------------#
b=10
if b >= 10:
    print('si es mayor o igual')
else:
    print('Es menor')

print(doble(1000))


