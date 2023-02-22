posfix = '5 6 2 + * 12 4 / -'
p = posfix.split()
def priority(c):
    if c in ['+','-']:
        return 1
    elif c in ['*','/']:
        return 2 
    elif c in ['^']:
        return 3
    elif c in ['(']:
        return 0

if p[0] in ['+','*','-','/']:
    print('operador')

p.append(')')
stack=[]
pos = 0
while p[pos] != ')':
    if type(p[pos]) == int:
        stack.append(p[pos])
    else:
        b = stack.pop()
        a = stack.pop()
        if p[pos] == '+':
            c = a + b 
        elif p[pos] == '-':
            c = a - b
        elif p[pos] == '*':
            c = a * b
        elif p[pos] == '/':
            c = a/b
        stack.append(c)
    pos+=1
value = stack.pop()
print(round((value)))

'''
while Q[n] != range(Q):
    if type(Q[n]) == 
'''