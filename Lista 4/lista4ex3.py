from random import randint

v1 = []
v2 = []
v_intercalado = []
x = 0

for k in range(10):
  x = randint(1, 100)
  v1.append(x)
  v_intercalado.append(x)

  x = randint(1, 100)
  v2.append(x)
  v_intercalado.append(x)

print(f'Vetor 1: {v1}')
print(f'Vetor 2: {v2}')
print(f'Vetor Intercalado: {v_intercalado}')