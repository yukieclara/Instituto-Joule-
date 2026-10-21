"""Testes do módulo 06. Rode com: pytest 06-arquivos-e-erros"""


def test_exercicio_01(carregar, tmp_path):
    m = carregar("exercicio_01.py")
    arq = tmp_path / "a.txt"
    arq.write_text("a\nb\nc\n", encoding="utf-8")
    assert m.ler_linhas(str(arq)) == ["a", "b", "c"]
    vazio = tmp_path / "vazio.txt"
    vazio.write_text("", encoding="utf-8")
    assert m.ler_linhas(str(vazio)) == []


def test_exercicio_02(carregar, tmp_path):
    m = carregar("exercicio_02.py")
    arq = tmp_path / "a.txt"
    arq.write_text("um\ndois\ntres\n", encoding="utf-8")
    assert m.contar_linhas(str(arq)) == 3
    vazio = tmp_path / "vazio.txt"
    vazio.write_text("", encoding="utf-8")
    assert m.contar_linhas(str(vazio)) == 0


def test_exercicio_03(carregar, tmp_path):
    m = carregar("exercicio_03.py")
    arq = tmp_path / "saida.txt"
    m.salvar_lista(str(arq), ["x", "y"])
    assert arq.read_text(encoding="utf-8") == "x\ny\n"
    m.salvar_lista(str(arq), [1, 2, 3])
    assert arq.read_text(encoding="utf-8") == "1\n2\n3\n"
    m.salvar_lista(str(arq), [])
    assert arq.read_text(encoding="utf-8") == ""


def test_exercicio_04(carregar):
    m = carregar("exercicio_04.py")
    assert m.ler_inteiro_seguro("42") == 42
    assert m.ler_inteiro_seguro(" 7 ") == 7
    assert m.ler_inteiro_seguro("-3") == -3
    assert m.ler_inteiro_seguro("abc") is None
    assert m.ler_inteiro_seguro("3.5") is None
    assert m.ler_inteiro_seguro("") is None


def test_exercicio_05(carregar, tmp_path):
    m = carregar("exercicio_05.py")
    arq = tmp_path / "n.txt"
    arq.write_text("1\n2\nabc\n3.5\n\n", encoding="utf-8")
    assert m.somar_arquivo(str(arq)) == 6.5
    assert m.somar_arquivo(str(tmp_path / "nao_existe.txt")) == 0


def test_exercicio_06(carregar, tmp_path):
    m = carregar("exercicio_06.py")
    arq = tmp_path / "d.json"
    dados = {"a": [1, 2], "b": "ção"}
    m.salvar_json(str(arq), dados)
    assert m.carregar_json(str(arq), None) == dados
    assert m.carregar_json(str(tmp_path / "nao_existe.json"), []) == []
    ruim = tmp_path / "ruim.json"
    ruim.write_text("{isso nao e json", encoding="utf-8")
    assert m.carregar_json(str(ruim), {"vazio": True}) == {"vazio": True}
