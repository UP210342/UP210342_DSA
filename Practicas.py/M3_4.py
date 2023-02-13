### LISTS 

#import Numpy as np
# c:\ pip install numpy
num = [10,5,7,9,2,8]
# print()numbers.sort())

# ordenado = sorted(num)
for i in range(0, len(num)):
    print(num[i], end = '\t')
print()
for i in num:
    print(i, end = '\t')
print()

num.append(18)
num.pop(2)
print(num)

name = 'Universidad'
r = name.replace('sida','vih')
print(r)

my_list = []
suma = 0
for i in range(5):
    my_list.append((i+1)*10)
    suma+=my_list[i]
print(my_list)
print(suma)
print(sum(my_list))

a = [10,20,30,40,50]

for i in range(len(a), 0):
    a = a[i]
print(a)
