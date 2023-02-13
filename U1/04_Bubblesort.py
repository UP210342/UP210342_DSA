def Bubblesort(vector):
    x = len(vector)
    swap = False 
    for i in range(x-1):
        for j in range(0,x-i-1):
            if vector[j] > vector[j+1]:
                swap = True
                vector[j], vector[j+1] = vector[j+1], vector[j]
    
vector = [45,79,421,56678,22,11,1]
Bubblesort(vector)
print(vector)