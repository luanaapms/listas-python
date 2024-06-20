a = int(input('Digite o lado a do seu triângulo: '))
b = int(input('Digite o lado b do seu triângulo: '))
c = int(input('Digite o lado c do seu triângulo: '))
if a > b + c or b > a + c or c > a + b:
  print ('Não é um triângulo!')
elif a == b == c: 
  print ('Triângulo Equilátero')
elif a == b or a == c or b == c:
  print ('Triângulo Isósceles')
else:
  print ('Triângulo Escaleno')