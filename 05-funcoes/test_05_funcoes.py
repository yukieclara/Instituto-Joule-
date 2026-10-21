"""Testes do módulo 05. Rode com: pytest 05-funcoes"""


def test_exercicio_01(carregar):
    m = carregar("exercicio_01.py")
    assert m.area_retangulo(3, 4) == 12
    assert m.area_retangulo(2.5, 2) == 5.0
    assert m.area_retangulo(0, 5) == 0


def test_exercicio_02(carregar):
    m = carregar("exercicio_02.py")
    for n in [2, 3, 5, 97, 7919]:
        assert m.eh_primo(n) is True, f"{n} é primo"
    for n in [-3, 0, 1, 4, 91, 100]:
        assert m.eh_primo(n) is False, f"{n} não é primo"


def test_exercicio_03(carregar):
    m = carregar("exercicio_03.py")
    assert m.maior_elemento([3, 9, 1]) == 9
    assert m.maior_elemento([-5, -2, -9]) == -2
    assert m.maior_elemento([7]) == 7
    assert m.maior_elemento([1.5, 2.5, 2.4]) == 2.5


def test_exercicio_04(carregar):
    m = carregar("exercicio_04.py")
    assert m.contar_palavras("a casa é azul") == 4
    assert m.contar_palavras("") == 0
    assert m.contar_palavras("  muitos   espaços  aqui ") == 3
    assert m.contar_palavras("oi") == 1


def test_exercicio_05(carregar):
    m = carregar("exercicio_05.py")
    assert m.fizzbuzz(15) == "FizzBuzz"
    assert m.fizzbuzz(30) == "FizzBuzz"
    assert m.fizzbuzz(3) == "Fizz"
    assert m.fizzbuzz(9) == "Fizz"
    assert m.fizzbuzz(5) == "Buzz"
    assert m.fizzbuzz(10) == "Buzz"
    assert m.fizzbuzz(7) == "7"
    assert m.fizzbuzz(1) == "1"


def test_exercicio_06(carregar):
    m = carregar("exercicio_06.py")
    assert m.eh_palindromo("arara") is True
    assert m.eh_palindromo("Ovo") is True
    assert m.eh_palindromo("Anotaram a data da maratona") is True
    assert m.eh_palindromo("python") is False
    assert m.eh_palindromo("") is True
