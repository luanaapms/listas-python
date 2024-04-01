s = float(input('Digite seu salário:'))
p = float(input('Porcentagem do aumento:'))

aumento = s * p /100
novo = s + aumento
print(f'Valor do aumento: R$ {aumento:}')
print(f'Novo salário: R$ {novo:}')