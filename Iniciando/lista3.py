'''
Cuidados com dados mutaveis
= - copiado o valor (imutaveis)
= - aponta para o mesmo valor na memoria (mutável)
'''

lista_a = ['Lucas', 'João', 'Bianca', 'Carlos']
lista_b = lista_a

lista_a[0] = 'Maria'

print(lista_b)


