nome = 'Lucas'
altura = 1.80
peso = 104
imc = peso / altura ** 2

# fStrings
linha_1 = f"{nome} tem {altura:,.2f} de altura e pesa {peso}kg e o seu IMC é {imc:,.2f}"

print(linha_1)

letras = 'abc'
print(f'{letras}')
print(f'{letras: >10}')
print(f'{letras: <10}')
print(f'{letras: ^10}')
print(f'{1000.5664451514842001831:.2f}')