def priority(c):
    if c in ['+','-']:
        return 1
    elif c in ['*','/']:
        return 2 
    elif c in ['^']:
        return 3
    elif c in ['(',')']:
        return 0

Q = '1 / ( x + 1 / ( x + 1 / ( x + 1 / x ) ) ) '
Q = Q.split()
Q.insert(0, '(')
Q.append(')')

pos = 0
P = []
stack = []
Operators = ['+','-','/','*','^']

for pos in range(len(Q)):
    if Q[pos] == '(':
        stack.append(Q[pos])
    elif Q[pos] in Operators:
        x = int(priority(stack[-1]))
        y = int(priority(Q[pos]))
        if x >= y:
            P.append(stack[-1])
            stack.pop()
        stack.append(Q[pos])
    elif Q[pos] == ')':
        while stack[-1] != '(':
            P.append(stack[-1])
            stack.pop()
        stack.pop()
    else:
        P.append(Q[pos])

print(P)