def par_impar(numero):

    multiplo = numero % 2 == 0

    if multiplo:
        return f'{numero} é par'
    return f'{numero} é ímpar'

print(par_impar(2))
print(par_impar(3))

print('---------------------------------')

def multiplicar(*args):

    total = 1
    for numero in args:
        total *= numero
    return total

multi = multiplicar(1,2,3,4,5)
print(multi)




