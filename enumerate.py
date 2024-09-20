'''
Enumerates - enumera iteraveis (indicies)
'''

nomes = ['Lucas', 'João', 'Bianca', 'Carlos']

lista_enumerada = list(enumerate(nomes))

for indice, nome in lista_enumerada:
    print(indice, nome)