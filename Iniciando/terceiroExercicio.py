# Faça um programa que peça o primeiro nome do usuario. Se o nome tiver 4 letras ou menos escreva 'Seu nome é curto', se tiver entre 5 e 6 escreva 'Seu nome é normal' , maior que 6 escreva 'Seu nome é muito grande'

entrada = input('Escreva o seu primeiro nome: ')

try: 
    nome = (entrada)

    if nome > 1:

        if nome <= 4:
            print(f'O nome {entrada} é curto')
        elif nome >= 5 and nome <= 6:
            print(f'O nome {entrada} é normal')
        else:
            print(f'O nome {entrada} é muito grande')

    else:
        print('Digite mais de uma letra')

except:
    print('Por favor, digite um nome valido')
