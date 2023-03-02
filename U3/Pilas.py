class Node:
    def __init__(self, dato) -> None:
        self.data = dato
        self.next = None 
    
    def getData(self):
        return self.data
    
    def setData(self, dato):
        self.data = dato

class Stack:
    def __init__(self) -> None:
        self.head = None
        self.size = 0
    
    def getSize(self):
        return self.size
    
    def isEmpty(self):
        return True if self.size == 0 else False

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        self.size += 1

    def Pop(self):
        self.size -= 1
        EraseNode = self.head.data
        self.head.data = None
        self.head = self.head.next

        return EraseNode        

    def Peek(self):
        LastNode = self.next.next.data
        return LastNode

nodo1 = Node('Jesus')
print(nodo1.data)
print(nodo1.getData())
print(nodo1.next,'\n')

nodo1.setData('Maria')
print(nodo1.getData())
print(nodo1.data,'\n')

nodo2 = Node("JOSE")

nodo1.next = nodo2
print(nodo1.data)

nodo3 = Node('Jesus')
nodo2.next = nodo3

print('------------')

print(nodo1.data)
print(nodo1.next.data)
print(nodo1.next.next.data)