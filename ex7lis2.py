metros = int(input('Digite a quantidade em metros de tinta a ser utilizada: '))
if metros % 18 == 0:
  latas = metros / 18
else:
  latas = int(metros / 18) + 1

preco = latas * 80

print (f'Quantidade de {latas} latas a serem compradas')
print (f'Preço total: R$ {preco:.2f}')