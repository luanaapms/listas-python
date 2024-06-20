valor = float(input("Quanto você recebe por hora?"))
hora = int(input("Quantas horas você trabalha?"))

sal_bruto = valor * hora
ir = sal_bruto * 0.11
inss = sal_bruto * 0.08
sind = sal_bruto * 0.05
sal_liquido = sal_bruto - ir - inss - sind

print(f'Salário Bruto: {sal_bruto}')
print(f'Desconto Imposto de Renda: {ir}')
print(f'Desconto INSS: {inss}')
print(f'Desconto Sindicato dos Trabalhadores: {sind}')
print(f'Salário Líquido: {sal_liquido}')


