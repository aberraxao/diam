from datetime import datetime
def _print(alinea: str) -> None:
    print(f'{10 * '-'} {alinea} {10 * '-'}')


def ex4():
    _print('4')
    _print('a - ii ordenada')
    print('amor vs roma:', transposicao_ordenada('amor', 'roma'))
    print('the alias men vs alan smithee:', transposicao_ordenada('the alias men', 'alan smithee'))
    print('batato vs batata:', transposicao_ordenada('batato', 'batata'))

    _print('a - i remocao')
    print('amor vs roma:', transposicao_pop('amor', 'roma'))
    print('the alias men vs alan smithee:', transposicao_pop('the alias men', 'alan smithee'))
    print('batato vs batata:', transposicao_pop('batato', 'batata'))


def transposicao_ordenada(palavra1: str, palavra2: str) -> bool:
    palavra1 = palavra1.replace(' ', '')
    palavra2 = palavra2.replace(' ', '')

    if sorted(palavra1) == sorted(palavra2):
        return True
    return False


def transposicao_pop(palavra1: str, palavra2: str) -> bool:
    palavra1 = palavra1.replace(' ', '')
    palavra2 = palavra2.replace(' ', '')

    for letra in palavra1:
        if letra in palavra2:
            palavra2 = palavra2.replace(letra, '', 1)

    if len(palavra2) > 0:
        return False
    return True


if __name__ == '__main__':
    ex4()
