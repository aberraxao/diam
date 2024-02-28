from typing import Dict, List


def _print(alinea: str) -> None:
    print(f'{10 * '-'} {alinea} {10 * '-'}')


def ex2():
    _print('2')
    _print('a')

    disciplinas_3ano_1semestre = {'AA': 19.89, 'AR': 19.5, 'PCD': 19.7, 'PI': 19.55}
    disciplinas_3ano_2semestre = {'DIAM': 20, 'ES': 19.7, 'IPM': 19.67, 'PISID': 19.9}

    print('disciplinas do semestre passado:', disciplinas_3ano_1semestre)
    print('disciplinas deste semestre:', disciplinas_3ano_2semestre)

    _print('b')
    disciplinas_3ano = disciplinas_3ano_1semestre | disciplinas_3ano_2semestre
    print('disciplinas do ano letivo:', disciplinas_3ano)

    _print('c')
    print('chaves:', list(disciplinas_3ano.keys()))

    _print('d')
    print('valores:', list(disciplinas_3ano.values()))

    _print('e')
    print('ordenado:', dict(sorted(disciplinas_3ano.items())))

    _print('f')
    existe_disciplina(disciplinas_3ano, 'DIAM')
    existe_disciplina(disciplinas_3ano, 'FRC')

    _print('g')
    print('notas acima de 19:', disciplinas_com_boas_notas(disciplinas_3ano, 19))
    print('notas acima de 19.7:', disciplinas_com_boas_notas(disciplinas_3ano, 19.7))

    _print('h')
    print('media das notas', media_das_notas(disciplinas_3ano))

    _print('i')
    print('tres melhores disciplinas', tres_melhores_disciplinas(disciplinas_3ano))


def existe_disciplina(disciplinas: Dict[str, float], nome: str) -> None:
    if nome in disciplinas.keys():
        print(f'{nome} existe no dicionario')
    else:
        print(f'{nome} nao existe no dicionario')


def disciplinas_com_boas_notas(disciplinas: Dict[str, float], nota_minima: float) -> List[str]:
    return [disciplina for disciplina, nota in disciplinas.items() if nota > nota_minima]


def media_das_notas(disciplinas: Dict[str, float]) -> float:
    return sum(disciplinas.values())/len(disciplinas)


def tres_melhores_disciplinas(disciplinas: Dict[str, float]) -> List[str]:
    return sorted(disciplinas, key=disciplinas.get)[-3:]


if __name__ == '__main__':
    ex2()
