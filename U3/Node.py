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
        LastNode = self.head.data

        return LastNode
    
stack = Stack()
stack.push('Yisus')
stack.push('Maria la del barrio')
stack.push('Pepe')

print(stack.Pop())
print(stack.Peek())