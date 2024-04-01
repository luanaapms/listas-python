from random import sample
num = sample(range(100), 20)

lista_par = []
lista_impar = []
x = 0

for x in num:
  if x % 2 == 0:
    lista_par.append(x)
  else:
    lista_impar.append(x)

print (f'Números {num}')
print (f'Pares {lista_par}')
print (f'Ímpares {lista_impar}')