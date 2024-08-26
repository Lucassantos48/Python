# Faça um programa que peça ao usuario para digitar um numero inteiro, informe se este número é par ou impar, caso o usuario não digite um numero inteiro , informe que que não é um numero inteiro

entrada = input('Digite um número: ')  
    
if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'Impar'
    
    if par_impar:
         par_impar_texto = 'Par'

    print(f'O número {entrada_int} é {par_impar_texto}')

else:
     print(f'O número digitado não é inteiro ')
