money = int(input('\n Give me the amount of money that you have: $'))
tickets = 0

while money > tickets:
    tickets += 1
    money -= tickets

print('\n You got',tickets,'tickets!')