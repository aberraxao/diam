def potencia(x, p=2):
    return x ** p


y = potencia(5, 3)

print(y)


def funcao_args(*args, x):
    print(type(args))
    print(args)


funcao_args(1, 2, x=3)


def funcao_kwargs(**kwargs):
    print(type(kwargs))
    print(kwargs)


funcao_kwargs(x=4, y=5)
