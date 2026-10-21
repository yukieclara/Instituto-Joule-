"""Testes do módulo 03. Rode com: pytest 03-repeticao"""


def test_exercicio_01(verificar):
    verificar("exercicio_01.py", [(['7'], ['7 x 1 = 7', '7 x 5 = 35', '7 x 10 = 70'], []),
     (['12'], ['12 x 1 = 12', '12 x 10 = 120'], [])])


def test_exercicio_02(verificar):
    verificar("exercicio_02.py", [(['10'], ['Soma: 55'], []), (['100'], ['Soma: 5050'], []), (['1'], ['Soma: 1'], [])])


def test_exercicio_03(verificar):
    verificar("exercicio_03.py", [(['5'], ['Fatorial: 120'], []),
     (['0'], ['Fatorial: 1'], []),
     (['10'], ['Fatorial: 3628800'], []),
     (['1'], ['Fatorial: 1'], [])])


def test_exercicio_04(verificar):
    verificar("exercicio_04.py", [(['3', '5', '2', '0'], ['Soma: 10', 'Quantidade: 3'], []),
     (['0'], ['Soma: 0', 'Quantidade: 0'], []),
     (['4', '0'], ['Soma: 4', 'Quantidade: 1'], []),
     (['-2', '8', '0'], ['Soma: 6', 'Quantidade: 2'], [])])


def test_exercicio_05(verificar):
    verificar("exercicio_05.py", [(['7'], ['primo'], ['composto']),
     (['12'], ['composto'], ['primo']),
     (['2'], ['primo'], ['composto']),
     (['97'], ['primo'], ['composto']),
     (['91'], ['composto'], ['primo']),
     (['9'], ['composto'], ['primo'])])


def test_exercicio_06(verificar):
    verificar("exercicio_06.py", [(['8'], ['0 1 1 2 3 5 8 13'], []),
     (['5'], ['0 1 1 2 3'], ['0 1 1 2 3 5']),
     (['2'], ['0 1'], ['0 1 1']),
     (['10'], ['0 1 1 2 3 5 8 13 21 34'], [])])
