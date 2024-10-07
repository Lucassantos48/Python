def criar_multiplicador(multiplicador):
    def multiplo(numero):
        return numero * multiplicador
    return multiplo

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))

