a = int(input('Numero a= '))
b = int(input('Numero b= '))
c = int(input('Numero c= '))


if a > b:
    print('a es mayor ')
else:
    if a > c:
        print('a es mayor')
    else: 
        if b > c:
            print('b es mayor')
        else:
            print('c es mayor')