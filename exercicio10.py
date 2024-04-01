cigarros = int(input('Quantidade de cigarros fumados por dia: '))
anos = int(input('Quantos anos você já fumou: '))

total_cigarros = anos * 365 * cigarros
dias = total_cigarros / 144
print(f'Você perdeu {dias: .1f} dias :(')