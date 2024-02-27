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


def ex1():
    print(f"{10 * '-'} 1a {10 * '-'}")
    lista_versos = poema.split(' / ')
    [print(verso) for verso in lista_versos]

    print(f"{10 * '-'} 1b {10 * '-'}")
    lista_versos += [
        'Por isso eu fiz um samba bem pra frente',
        'Dizendo realmente o que é que eu acho',
        'Isso me deixa triste e cabisbaixo'
    ]

    print(f"{10 * '-'} 1c {10 * '-'}")
    print(lista_versos[-2])
    print(lista_versos[-1])

    print(f"{10 * '-'} 1d {10 * '-'}")
    numero_versos_com_samba = 0
    for verso in lista_versos:
        if 'samba' in verso:
            numero_versos_com_samba += 1
    print('numero de versos com a palavra "samba":', numero_versos_com_samba)

    print(f"{10 * '-'} 1e {10 * '-'}")
    for vogal in ['a', 'e', 'i', 'o', 'u']:
        conta = 0
        for verso in lista_versos:
            if vogal in verso:
                conta += verso.lower().count(vogal)

        print(vogal, ':', conta)


if __name__ == "__main__":
    ex1()
