def validar(func):
    def valida(x,y):
        return func(x,y)

    return valida

@validar
def soma(x, y):
    return x + y

soma(10,20)