'''
Closure e funções que retornam outras funções.
'''

def criar_saudacao(saudacao): 
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

criando_saudacao = criar_saudacao('Boa tarde')

for nome in ['Lucas', 'Maria', 'João']:
    print(criando_saudacao(nome))