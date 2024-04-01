peso = float(input('Digite o peso dos peixes:'))

if peso > 50:
    excesso = peso - 50 
    multa = excesso * 4
else:
    excesso = multa = 0

print(f'Peso de excesso: {excesso}')
print(f'Multa no valor de R$: {multa}')


    