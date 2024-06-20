import random

numeros = [random.randint(1, 100) for k in range(10)]

maior = numeros[0]
menor = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero
    if numero < menor:
       menor = numero


print(numeros)
print(maior)
print(menor)