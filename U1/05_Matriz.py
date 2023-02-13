import numpy as np
from random import randint

def fillArr(x):
  arr = []

  for f in range(x):
    fil = []

    for c in range(x):
      fil.append(randint(1,1999))

    arr.append(fil)

  return arr

dim = int(input('Ingrese la dimension de su matriz: '))
matriz = np.array(fillArr(dim))
print(matriz)