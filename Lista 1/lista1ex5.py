m = float(input('Digite o preço da mercadoria:'))
p = float(input('Porcentagem de desconto:'))

desconto = m * p /100
novo = m - desconto
print(f'Valor do desconto: R$ {desconto:}')
print(f'Preço a pagar: R$ {novo:}')