from typing import List


def _print(alinea: str) -> None:
    print(f'{10 * '-'} {alinea} {10 * '-'}')


def ex3():
    _print('3')
    _print('a')

    lista_desordenada = [7, 4, 5, 9, 8, 2, 1, 3, 6, 10]
    print('lista desordenada:', lista_desordenada)

    lista_ordenada = selection_sort(lista_desordenada)
    print('lista ordenadas:', lista_ordenada)

    _print('b')
    lista_desordenada = [7, 4, 5, 9, 8, 2, 1, 3, 6, 10]
    print('lista desordenada:', lista_desordenada)

    lista_ordenada = selection_sort_pythonica(lista_desordenada)
    print('lista ordenadas:', lista_ordenada)


def selection_sort(lista: list) -> List[int]:
    for i in range(0, len(lista)):
        min_index = i

        for j in range(i + 1, len(lista)):
            # seleciona o minimo
            if lista[j] < lista[min_index]:
                min_index = j

        # faz a troca
        temp = lista[i]
        lista[i] = lista[min_index]
        lista[min_index] = temp

    return lista


def selection_sort_pythonica(lista: list) -> List[int]:
    for i in range(0, len(lista)):
        min_index = i

        for j in range(i + 1, len(lista)):
            # seleciona o minimo
            if lista[j] < lista[min_index]:
                min_index = j

        # faz a troca
        lista[i], lista[min_index] = lista[min_index], lista[i]

    return lista


if __name__ == '__main__':
    ex3()
