# Módulo 07: Projeto, gerenciador de tarefas no terminal

Agora você junta tudo o que aprendeu em um programa de verdade: uma lista de tarefas que roda no terminal e **guarda os dados em arquivo**, então as tarefas continuam lá quando você fecha e abre de novo.

Você vai usar listas, dicionários, condicionais, laços, funções, arquivos e JSON.

## Como o programa vai funcionar

```text
=== Minhas tarefas ===
1. Adicionar tarefa
2. Listar tarefas pendentes
3. Listar todas as tarefas
4. Concluir tarefa
5. Remover tarefa
0. Sair
Escolha: 1
Título da tarefa: Estudar para a prova
Tarefa 1 adicionada.
```

Cada tarefa é um dicionário:

```python
{"id": 1, "titulo": "Estudar para a prova", "concluida": False}
```

E a lista de tarefas é uma lista desses dicionários.

## Os arquivos

| Arquivo | Função |
|---|---|
| `tarefas.py` | A **lógica**: criar, concluir, remover e listar tarefas. Não tem `input` nem `print`. |
| `armazenamento.py` | Salvar e carregar a lista em um arquivo JSON. |
| `main.py` | O **menu**: pergunta o que a pessoa quer fazer e chama as funções acima. |
| `test_projeto_tarefas.py` | Os testes da lógica e do armazenamento. |

Separar a lógica (que decide) da interface (que conversa com a pessoa) é uma das ideias mais importantes da programação. Repare que é por isso que dá para testar `tarefas.py` sem digitar nada.

## Etapa 1: a lógica (`tarefas.py`)

Implemente as quatro funções, seguindo os comentários do arquivo:

- `criar_tarefa(tarefas, titulo)`
- `concluir_tarefa(tarefas, id_tarefa)`
- `remover_tarefa(tarefas, id_tarefa)`
- `listar_pendentes(tarefas)`

Teste: `pytest 07-projeto-tarefas -k "criar or concluir or remover or pendentes"`

**Definição de pronto:** os testes dessas funções passam.

## Etapa 2: o menu (`main.py`)

Escreva o laço do menu: mostrar as opções, ler a escolha, chamar a função certa e mostrar o resultado para a pessoa. Por enquanto, a lista fica só na memória (some ao fechar).

Aqui não tem teste automático: teste na mão, tentando também os casos chatos (concluir uma tarefa que não existe, digitar uma letra no lugar do número, título vazio). O programa **não pode quebrar**.

**Definição de pronto:** você usa o programa por 5 minutos tentando quebrar e não consegue.

## Etapa 3: salvar em arquivo (`armazenamento.py`)

Implemente `salvar(tarefas, caminho)` e `carregar(caminho)`. No `main.py`, carregue as tarefas ao abrir e salve depois de cada mudança. Se o arquivo ainda não existe, `carregar` devolve uma lista vazia.

Teste: `pytest 07-projeto-tarefas -k "salvar or carregar"`

**Definição de pronto:** você adiciona tarefas, fecha o programa, abre de novo e elas continuam lá.

## Etapa 4: melhorias (escolha pelo menos duas)

Agora o projeto é seu. Algumas ideias, da mais simples para a mais difícil:

- Mostrar no fim da listagem `X de Y tarefas concluídas`
- Editar o título de uma tarefa
- Buscar tarefas por uma palavra do título
- Dar prioridade (alta, média, baixa) e listar da mais importante para a menos
- Ter data limite e mostrar primeiro as que vencem antes
- Exportar as tarefas para um arquivo CSV
- Receber comandos pela linha de comando com o módulo `argparse` (por exemplo `python main.py adicionar "Estudar"`)

Para cada melhoria, **crie uma issue no GitHub** descrevendo o que vai fazer e **uma branch própria**. Isso é o que se faz em projetos reais.

## Etapa 5: testes, README e revisão

1. **Escreva pelo menos 2 testes novos** em `test_projeto_tarefas.py` para a(s) melhoria(s) que você criou. Olhe os testes existentes como modelo.
2. **Escreva o README do seu projeto** (substitua o texto deste arquivo na sua cópia): o que o programa faz, como rodar, um exemplo de uso e o que você aprendeu.
3. **Abra o pull request final** e peça a revisão do mentor.

## Desafio bônus

Reescreva a **Etapa 1 em C** (dica: use uma `struct` para a tarefa e um vetor de structs). Compare o tamanho e a dificuldade das duas versões. O que ficou mais fácil em Python? O que o C te obrigou a pensar que o Python esconde?

## Como contar isso no currículo

Quando terminar, uma frase como esta já fica boa (adapte para o que você realmente fez):

> Desenvolvi em Python um gerenciador de tarefas em linha de comando, com persistência em JSON, separação entre lógica e interface e testes automatizados com pytest.

Coloque o link do repositório no currículo e no LinkedIn.
