from datetime import datetime
from typing import List


def _print(alinea: str) -> None:
    print(f'{10 * '-'} {alinea} {10 * '-'}')


def ex4():
    _print('4')
    _print('amor vs roma')
    print(transposicao_ordenada('amor', 'roma'))
    print(transposicao_pop('amor', 'roma'))

    _print('the alias men vs alan smithee')
    print(transposicao_ordenada('the alias men', 'alan smithee'))
    print(transposicao_pop('the alias men', 'alan smithee'))

    _print('batato vs batata')
    print(transposicao_ordenada('batato', 'batata'))
    print(transposicao_pop('batato', 'batata'))


def selection_sort_pythonica(lista: list, passos: int) -> (List[str], int):
    for i in range(0, len(lista)):
        passos += 1
        min_index = i

        for j in range(i + 1, len(lista)):
            passos += 1
            # seleciona o minimo
            if lista[j] < lista[min_index]:
                min_index = j

        # faz a troca
        lista[i], lista[min_index] = lista[min_index], lista[i]

    return lista, passos


def transposicao_ordenada(palavra1: str, palavra2: str) -> bool:
    palavra1 = list(palavra1.replace(' ', ''))
    palavra2 = list(palavra2.replace(' ', ''))

    passos, start = 0, datetime.now()
    palavra1_ordenada, passos = selection_sort_pythonica(palavra1, passos)
    palavra2_ordenada, passos = selection_sort_pythonica(palavra2, passos)
    td = (datetime.now() - start).total_seconds() * 10 ** 3

    print(f'ii - tranposicao ordenada: {passos} loops, {td:.03f}ms')

    if palavra1_ordenada == palavra2_ordenada:
        return True
    return False


def transposicao_pop(palavra1: str, palavra2: str) -> bool:
    palavra1 = list(palavra1.replace(' ', ''))
    palavra2 = list(palavra2.replace(' ', ''))

    passos, start = 0, datetime.now()
    for letra in palavra1:
        passos += 1
        for i in range(0, len(palavra2)):
            passos += 1
            if palavra2[i] == letra:
                palavra2.pop(i)
                break
    td = (datetime.now() - start).total_seconds() * 10 ** 3

    print(f'i - tranposicao retirada: {passos} loops, {td:.03f}ms')

    if len(palavra2) > 0:
        return False
    return True


if __name__ == '__main__':
    ex4()
