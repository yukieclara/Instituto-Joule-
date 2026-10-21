"""Menu do gerenciador de tarefas.

Aqui é onde ficam o input() e o print(). A lógica de verdade está em tarefas.py.

Roteiro:
1. Importe as funções de tarefas.py (e depois de armazenamento.py).
2. Crie a lista de tarefas (começa vazia; na etapa 3, carregada do arquivo).
3. Faça um laço (while True) que mostra o menu, lê a opção e chama a função certa.
4. Trate as entradas inválidas (letra no lugar de número, id que não existe, título vazio).
   O programa não pode quebrar com erro.
5. A opção 0 sai do laço.
"""
from tarefas import criar_tarefa, concluir_tarefa, remover_tarefa, listar_pendentes


def main():
    pass


if __name__ == "__main__":
    main()
