import random

lista = []
maior_valor = 0
menor_valor = 100
j = 0
k = 0

while len(lista) < 10:
    lista.append(random.randint(1, 100))

for i in lista:
    print(i)

while j < 10:
    if lista [j] > maior_valor:
        maior_valor = lista[j]
    else:
        maior_valor = maior_valor
        j += 1 

while k < 10:
    if lista [k] > menor_valor:
        menor_valor = lista[k]
    else:
        menor_valor = menor_valor
        k += 1 

print(f'O maior valor é {maior_valor}')
print(f'O menor valor é {menor_valor}')