P = [5,6,2,'+','*',12,4,'/','-']
Operands = ['+','-','*','/']
P.append(')')
stack=[]
pos = 0
while P[pos] != ')':
    if type(P[pos]) == int:
        stack.append(P[pos])
    else:
        b = stack.pop()
        a = stack.pop()
        if P[pos] == '+':
            c = a + b 
        elif P[pos] == '-':
            c = a - b
        elif P[pos] == '*':
            c = a * b
        elif P[pos] == '/':
            c = a/b
        stack.append(c)
    pos+=1
value = stack.pop()
print(round((value)))

'''
for Q[n] in range(Q):
    if Q[n] != Operands & '()':
        int(Q[n])
'''