num = int(input('Digite um número inteiro:'))

a, b = 1, 1
k = 1

while k <= num -2:
    a, b = b, a + b
    k = k + 1

print(f'Fibonacci: {b}')