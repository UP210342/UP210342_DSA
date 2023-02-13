palabra = input('Dame una palabra y te dire si es palindromo o no:' )

change = palabra.replace(" "," ")
change = change.lower()

palabra_inversa = change[::-1]
print(change)
print(palabra_inversa)

if change == palabra_inversa:
     print('Si es palindromo')
else: 
    print('No es palindromo')
