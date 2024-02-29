poema = (
    'Eu hoje fiz um samba bem pra frente / Dizendo realmente o que é que eu '
    'acho / Eu acho que o meu samba é uma corrente / E coerentemente assino embaixo '
    '/ Hoje é preciso refletir um pouco / E ver que o samba está tomando jeito / Só '
    'mesmo embriagado ou muito louco / Pra contestar e pra botar defeito / Precisa '
    'ser muito sincero e claro / Pra confessar que andei sambando errado / Talvez '
    'precise até tomar na cara / Pra ver que o samba está bem melhorado / Tem mais é '
    'que ser bem cara de tacho / Não ver a multidão sambar contente / Isso me deixa '
    'triste e cabisbaixo / Por isso eu fiz um samba bem pra frente / Dizendo realmente '
    'o que é que eu acho / Eu acho que o meu samba é uma corrente / E coerentemente '
    'assino embaixo / Hoje é preciso refletir um pouco / E ver que o samba está '
    'tomando jeito / Só mesmo embriagado ou muito louco / Pra contestar e pra botar '
    'defeito / Precisa ser muito sincero e claro / Pra confessar que andei sambando '
    'errado / Talvez precise até tomar na cara / Pra ver que o samba está bem melhorado '
    '/ Tem mais é que ser bem cara de tacho / Não ver a multidão sambar contente / '
    'Isso me deixa triste e cabisbaixo'
)


def _print(alinea: str) -> None:
    print(f'{10 * "-"} {alinea} {10 * "-"}')


def ex1() -> None:
    _print('1')
    _print('a')
    lista_versos = poema.split(' / ')
    [print(verso) for verso in lista_versos]

    _print('b')
    lista_versos += [
        'Por isso eu fiz um samba bem pra frente',
        'Dizendo realmente o que é que eu acho',
        'Isso me deixa triste e cabisbaixo'
    ]
    [print(verso) for verso in lista_versos]

    _print('c')
    print(lista_versos[-2])
    print(lista_versos[-1])

    _print('d')
    count = 0
    for verso in lista_versos:
        if 'samba' in verso:
            count += 1
    print('Número de versos com a palavra "samba":', count)

    _print('e')
    for vogal in ['a', 'e', 'i', 'o', 'u']:
        total = sum(verso.lower().count(vogal) for verso in lista_versos if vogal in verso)
        print(vogal, ':', total)


if __name__ == '__main__':
    ex1()
