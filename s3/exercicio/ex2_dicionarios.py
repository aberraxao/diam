def _print(alinea: str) -> None:
    print(f"{10 * '-'} {alinea} {10 * '-'}")


def ex2():
    _print("2")
    _print("a")

    disciplinas_3ano_1semestre = {"AA": 19.89, "AR": 19.5, "PCD": 19.7, "PI": 19.55}
    disciplinas_3ano_2semestre = {"DIAM": 20, "ES": 19.7, "IPM": 19.67, "PISID": 19.9}

    print('disciplinas do semestre passado:', disciplinas_3ano_1semestre)
    print('disciplinas deste semestre:', disciplinas_3ano_2semestre)

    _print("b")
    disciplinas_3ano = disciplinas_3ano_1semestre | disciplinas_3ano_2semestre
    print('disciplinas do ano letivo:', disciplinas_3ano)

    _print("c")
    print("chaves:", list(disciplinas_3ano.keys()))

    _print("d")
    print("valores:", list(disciplinas_3ano.values()))

    _print("e")  # TODO: dúvida: é necessário mostrar as notas?
    print("ordenado:", sorted(disciplinas_3ano.keys()))


if __name__ == "__main__":
    ex2()
