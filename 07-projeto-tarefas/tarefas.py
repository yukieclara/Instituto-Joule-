"""Lógica do gerenciador de tarefas. Aqui NÃO tem input nem print.

Cada tarefa é um dicionário:  {"id": 1, "titulo": "Estudar", "concluida": False}
A lista de tarefas é uma lista desses dicionários.
"""


def criar_tarefa(tarefas, titulo):
    """Cria uma tarefa nova e a adiciona na lista `tarefas`.

    - O título deve ser guardado sem espaços sobrando no começo e no fim.
    - Se o título estiver vazio (ou só com espaços), levante ValueError.
    - O id é o maior id existente + 1 (ou 1 se a lista estiver vazia).
    - A tarefa nova começa com concluida=False.
    - Devolve a tarefa criada.
    """
    pass


def concluir_tarefa(tarefas, id_tarefa):
    """Marca a tarefa como concluída. Devolve True se achou a tarefa, False se não existe."""
    pass


def remover_tarefa(tarefas, id_tarefa):
    """Remove a tarefa da lista. Devolve True se removeu, False se não existe."""
    pass


def listar_pendentes(tarefas):
    """Devolve uma nova lista só com as tarefas que ainda não foram concluídas."""
    pass
