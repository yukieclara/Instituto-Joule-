"""Testes do módulo 02. Rode com: pytest 02-condicionais"""


def test_exercicio_01(verificar):
    verificar("exercicio_01.py", [(['4'], ['par'], ['impar']),
     (['7'], ['impar'], []),
     (['0'], ['par'], ['impar']),
     (['-3'], ['impar'], [])])


def test_exercicio_02(verificar):
    verificar("exercicio_02.py", [(['1', '5', '3'], ['Maior: 5'], []),
     (['9', '2', '4'], ['Maior: 9'], []),
     (['2', '2', '7'], ['Maior: 7'], []),
     (['-1', '-5', '-3'], ['Maior: -1'], [])])


def test_exercicio_03(verificar):
    verificar("exercicio_03.py", [(['8'], ['aprovado'], ['recuperacao', 'reprovado']),
     (['7'], ['aprovado'], ['recuperacao', 'reprovado']),
     (['6.5'], ['recuperacao'], ['aprovado', 'reprovado']),
     (['5'], ['recuperacao'], ['aprovado', 'reprovado']),
     (['4.9'], ['reprovado'], ['aprovado', 'recuperacao']),
     (['0'], ['reprovado'], ['aprovado', 'recuperacao'])])


def test_exercicio_04(verificar):
    verificar("exercicio_04.py", [(['2024'], ['bissexto'], ['comum']),
     (['2023'], ['comum'], ['bissexto']),
     (['1900'], ['comum'], ['bissexto']),
     (['2000'], ['bissexto'], ['comum'])])


def test_exercicio_05(verificar):
    verificar("exercicio_05.py", [(['3', '3', '3'], ['equilatero'], ['isosceles', 'escaleno', 'invalido']),
     (['3', '3', '5'], ['isosceles'], ['equilatero', 'escaleno', 'invalido']),
     (['3', '4', '5'], ['escaleno'], ['equilatero', 'isosceles', 'invalido']),
     (['1', '2', '10'], ['invalido'], ['equilatero', 'isosceles', 'escaleno']),
     (['5', '3', '3'], ['isosceles'], ['invalido'])])


def test_exercicio_06(verificar):
    verificar("exercicio_06.py", [(['6', '*', '7'], ['Resultado: 42.0'], ['Erro']),
     (['10', '/', '4'], ['Resultado: 2.5'], ['Erro']),
     (['5', '-', '8'], ['Resultado: -3.0'], ['Erro']),
     (['2', '+', '2'], ['Resultado: 4.0'], ['Erro']),
     (['8', '/', '0'], ['Erro'], ['Resultado']),
     (['8', '%', '3'], ['Erro'], ['Resultado'])])
