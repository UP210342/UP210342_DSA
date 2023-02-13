c0 = 1000
i = 0
while c0 != 1:
    if c0 % 2 == 0: #par
        c0 /= 2
        print(c0)
    elif c0 % 2 != 0: #par
        c0 = (3 * c0) + 1
        print(c0)
    i += 1
print('steps: ',i)
    