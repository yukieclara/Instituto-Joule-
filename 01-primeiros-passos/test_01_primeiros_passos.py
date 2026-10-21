"""Testes do módulo 01. Rode com: pytest 01-primeiros-passos"""


def test_exercicio_01(verificar):
    verificar("exercicio_01.py", [(['Ana'], ['Olá, Ana!'], []), (['Pedro'], ['Olá, Pedro!'], [])])


def test_exercicio_02(verificar):
    verificar("exercicio_02.py", [(['3', '4'], ['Soma: 7'], []), (['-2', '10'], ['Soma: 8'], []), (['0', '0'], ['Soma: 0'], [])])


def test_exercicio_03(verificar):
    verificar("exercicio_03.py", [(['7', '8', '9'], ['Média: 8.00'], []),
     (['5', '5', '6'], ['Média: 5.33'], []),
     (['10', '10', '10'], ['Média: 10.00'], [])])


def test_exercicio_04(verificar):
    verificar("exercicio_04.py", [(['100'], ['Fahrenheit: 212.0'], []),
     (['0'], ['Fahrenheit: 32.0'], []),
     (['37'], ['Fahrenheit: 98.6'], [])])


def test_exercicio_05(verificar):
    verificar("exercicio_05.py", [(['17', '5'], ['Quociente: 3', 'Resto: 2'], []),
     (['20', '4'], ['Quociente: 5', 'Resto: 0'], []),
     (['3', '7'], ['Quociente: 0', 'Resto: 3'], [])])


def test_exercicio_06(verificar):
    verificar("exercicio_06.py", [(['3725'], ['Tempo: 1:02:05'], []),
     (['59'], ['Tempo: 0:00:59'], []),
     (['86399'], ['Tempo: 23:59:59'], []),
     (['3600'], ['Tempo: 1:00:00'], [])])
