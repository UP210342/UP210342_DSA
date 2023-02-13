import random

shh = random.randint(1,100)
num = 0
print(
"""
+===============================+
|   WELCOME TO MY SECRET GAME   |
|  Enter an integer number  and |
|  guess the number i've picked |
|  for you.                     |
|                               |
|  WHAT'S THE SECRET NUMBER???  |
+===============================+
\n
"""
)

while num != shh:
    num = int(input('Give me your guess: '))
    if num == shh:
        print('\nCongrats, you guessed right!')
    elif num < shh:
        print('\nHot...')
    elif num > shh:
        print('\nCold...')