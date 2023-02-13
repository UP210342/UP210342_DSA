Q = '( 5 * ( 6 + 2 ) - 12 / 4 )'
Q.append('.')
Q = Q.split()
print(Q)
pos = 0
P = []
stack = []
Operands = ['+','-','*','/','(',')']
Num = []

while P[pos] != '.':
    if Q[pos] != Operands:
        Num.append(Q[pos])
    pos += 1

