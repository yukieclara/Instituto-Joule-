"""Testes do projeto. Rode com: pytest 07-projeto-tarefas

Estes testes cobrem as Etapas 1 e 3. Na Etapa 5 você vai acrescentar os seus.
"""
import pytest


def test_criar_tarefa(carregar):
    t = carregar("tarefas.py")
    tarefas = []
    primeira = t.criar_tarefa(tarefas, "Estudar Python")
    assert primeira == {"id": 1, "titulo": "Estudar Python", "concluida": False}
    assert tarefas == [primeira]
    segunda = t.criar_tarefa(tarefas, "  Lavar a louça  ")
    assert segunda["id"] == 2
    assert segunda["titulo"] == "Lavar a louça"
    assert len(tarefas) == 2


def test_criar_tarefa_titulo_vazio(carregar):
    t = carregar("tarefas.py")
    tarefas = []
    with pytest.raises(ValueError):
        t.criar_tarefa(tarefas, "   ")
    assert tarefas == []


def test_criar_tarefa_id_depois_de_remover(carregar):
    t = carregar("tarefas.py")
    tarefas = []
    t.criar_tarefa(tarefas, "a")
    t.criar_tarefa(tarefas, "b")
    t.remover_tarefa(tarefas, 1)
    nova = t.criar_tarefa(tarefas, "c")
    assert nova["id"] == 3


def test_concluir_tarefa(carregar):
    t = carregar("tarefas.py")
    tarefas = []
    t.criar_tarefa(tarefas, "a")
    t.criar_tarefa(tarefas, "b")
    assert t.concluir_tarefa(tarefas, 2) is True
    assert tarefas[1]["concluida"] is True
    assert tarefas[0]["concluida"] is False
    assert t.concluir_tarefa(tarefas, 99) is False


def test_remover_tarefa(carregar):
    t = carregar("tarefas.py")
    tarefas = []
    t.criar_tarefa(tarefas, "a")
    t.criar_tarefa(tarefas, "b")
    assert t.remover_tarefa(tarefas, 1) is True
    assert [x["titulo"] for x in tarefas] == ["b"]
    assert t.remover_tarefa(tarefas, 1) is False


def test_listar_pendentes(carregar):
    t = carregar("tarefas.py")
    tarefas = []
    t.criar_tarefa(tarefas, "a")
    t.criar_tarefa(tarefas, "b")
    t.criar_tarefa(tarefas, "c")
    t.concluir_tarefa(tarefas, 2)
    pendentes = t.listar_pendentes(tarefas)
    assert [x["titulo"] for x in pendentes] == ["a", "c"]
    assert len(tarefas) == 3  # a lista original não pode mudar


def test_salvar_e_carregar(carregar, tmp_path):
    a = carregar("armazenamento.py")
    caminho = str(tmp_path / "t.json")
    tarefas = [{"id": 1, "titulo": "Estudar ação", "concluida": False}]
    a.salvar(tarefas, caminho)
    assert a.carregar(caminho) == tarefas


def test_carregar_sem_arquivo(carregar, tmp_path):
    a = carregar("armazenamento.py")
    assert a.carregar(str(tmp_path / "nao_existe.json")) == []
