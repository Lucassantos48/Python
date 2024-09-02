while True:

    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')
    num_1_float = 0
    num_2_float = 0
    numeros_validos = None

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
    
    if numeros_validos is None: 
        print('Um ou ambos os números são invalidos.')
        continue
    
    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue
    
    print('Realizando a sua conta. Confira o resultado abaixo: ')
    if operador == '+':
        print(num_1_float + num_2_float)
    
    elif operador == '-':
        print(num_1_float - num_2_float)

    elif operador == '/':
        print(num_1_float / num_2_float)

    elif operador == '*':
        print(num_1_float * num_2_float)

    else:
        print('Não deveria chegar aqui.')

    sair = input('Quer sair? [S]air: ').lower().startswith('s')

    if sair is True:
        break