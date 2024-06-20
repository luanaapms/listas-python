lista_pardiv = []

for number in range(1067, 3628):
    if number % 2 == 0 and number % 7 == 0:
        lista_pardiv.append(number)

print(len(lista_pardiv))