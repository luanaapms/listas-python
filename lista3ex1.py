nota = float(input('Digite sua nota de 0 a 10:'))

while nota > 10 or nota < 0:
    print('Essa nota não é válida! Notas entre 0 e 10.')
    nota = float(input('Digite uma nota: '))
    print(f'Nota válida! Sua nota é {nota}')
