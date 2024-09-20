
def nome(nome):
    print(f'Seja bem-vindo, {nome}!')

nome('Lucas')
nome('Maria')

def soma(x, y, z=None):

    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)

print(10, 20)
print(10, 20, 30)

