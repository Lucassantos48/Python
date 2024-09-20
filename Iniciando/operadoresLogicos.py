#  Operadores lógicos and, or e not
#  Operadores in e not in
#  A senha vem de um banco de dados, a senha usada é para estudo

nome = input('Digite o seu nome: ')
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Digite a senha: ')

senha_permitida = '12345'
if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print(f'Bem vindo: {nome}')
else:
    print('Sair')

# Avaliação de curto circuito
senha = input('Digite a senha: ') or 'Sem senha'
print(senha)

senha_teste = input('Senha: ')

# O not inverte se é True vira False e se é False vira True
if not senha: 
    print('Senha incorreta')

print(not True) #False
print(not False) #True

nomes = 'Lucas'
print('c' in nomes) #True
print('b' in nomes) #False
print('c' not in nomes) #False