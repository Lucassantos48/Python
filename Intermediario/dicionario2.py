# Manipulando chaves e valores em dicionarios

pessoa = {
    'nome': 'Lucas',
    'sobrenome': 'Marques',
    'idade': 23,
    'altura': 1.8,
    'endereços': [
        {'Rua': 'Geronimo', 'número': 123}
    ],
}

# print(len(pessoa))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))

# for chave in pessoa:
#     print(chave)

for valor in pessoa.values():
    print(valor)
