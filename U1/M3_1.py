a = 1 == 1.
print(a)
a = 0
print(a != 0)

#----------------------#

for i in range(10):
    pass 
    continue
    break
    print(hola)
print('Fin')

#----------------------#

user_word = input('Give me a word: ')
user_word = user_word.upper()
new_word = ' '

#----------------------#

for letter in user_word:
    if letter not in ('A,E,I,O,U'):
        new_word += letter
print(new_word)

#----------------------#

# Bit wise operators:
# & - bitwise conjuction 
# | bitwise disconjuction
# ~ bitwise negation
# ^ bitwise exclusive 

i = 34
j = 22
bit = i & j
print(bit)
print(~bit)

print(i>>1)
print(i<<3)