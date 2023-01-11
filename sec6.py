import os 
import time

print('What is your last name?')
lastName = input()

Name = input('What is your name: ')

Edad = int(input('Give me a number: '))
print(type(Edad))

comp_name = Name + ' ' + lastName

print('Your full name is', comp_name, '\n Your number is: ', Edad)
print('Hola'*2, 2*'Adios')

