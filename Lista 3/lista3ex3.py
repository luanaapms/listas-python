pop_a = 8000
pop_b = 20000
ano = 0

while pop_a < pop_b:
     
  pop_a = pop_a + pop_a * 0.03
  pop_b = pop_b + pop_b * 0.015
  ano = ano + 1

print(f'Será necessário {ano} anos para a população A ultrapassar a de B.')