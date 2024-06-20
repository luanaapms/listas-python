usuario = str(input('Digite o nome de usuário: '))
senha = str(input('Digite a senha: '))

while usuario == senha:
  
  print('ERRO! Sua senha deve ser diferente do usuário')
  usuario = str(input('Usuário: '))
  senha = str(input('Senha: '))
  print('Cadastro realizado com sucesso!')
