"""Testes do módulo 04. Rode com: pytest 04-listas-textos-dicionarios"""


def test_exercicio_01(verificar):
    verificar("exercicio_01.py", [(['3', '9', '1', '7', '5'], ['Maior: 9', 'Menor: 1'], []),
     (['-1', '-8', '0', '4', '2'], ['Maior: 4', 'Menor: -8'], []),
     (['5', '5', '5', '5', '5'], ['Maior: 5', 'Menor: 5'], [])])


def test_exercicio_02(verificar):
    verificar("exercicio_02.py", [(['python'], ['nohtyp'], []), (['abc'], ['cba'], []), (['Ana e Bia'], ['aiB e anA'], [])])


def test_exercicio_03(verificar):
    verificar("exercicio_03.py", [(['Programacao'], ['Vogais: 5'], []),
     (['AEIOU'], ['Vogais: 5'], []),
     (['rhythm'], ['Vogais: 0'], []),
     (['Banana'], ['Vogais: 3'], [])])


def test_exercicio_04(verificar):
    verificar("exercicio_04.py", [(['arara'], ['sim'], ['nao']),
     (['python'], ['nao'], ['sim']),
     (['Ovo'], ['sim'], ['nao']),
     (['a'], ['sim'], ['nao']),
     (['casa'], ['nao'], ['sim'])])


def test_exercicio_05(verificar):
    verificar("exercicio_05.py", [(['a casa e a porta'], ['a: 2', 'casa: 1', 'e: 1', 'porta: 1'], []),
     (['Sol sol SOL lua'], ['sol: 3', 'lua: 1'], []),
     (['oi'], ['oi: 1'], [])])


def test_exercicio_06(verificar):
    verificar("exercicio_06.py", [(['1 2 2 3 1'], ['1 2 3'], ['1 2 2']),
     (['5 5 5'], ['5'], ['5 5']),
     (['4 3 4 1 3'], ['4 3 1'], ['4 3 4'])])
