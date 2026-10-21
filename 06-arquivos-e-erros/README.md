# Módulo 06: Arquivos, erros e JSON

## O que você vai aprender

- Ler e escrever arquivos de texto
- Tratar erros com `try` e `except`
- Guardar dados estruturados em JSON

Esse módulo prepara o terreno para o projeto final, onde as tarefas vão ser salvas em arquivo.

## Lendo e escrevendo arquivos

Use sempre `with`: ele fecha o arquivo sozinho, mesmo se acontecer um erro.

```python
# escrever (o "w" apaga o que já existia)
with open("notas.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("10\n")
    arquivo.write("8.5\n")

# ler tudo de uma vez
with open("notas.txt", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

# ler linha a linha
with open("notas.txt", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())      # strip() tira o \n do fim
```

Modos principais: `"r"` (ler, padrão), `"w"` (escrever, apagando) e `"a"` (acrescentar no fim). O `encoding="utf-8"` evita problemas com acentos.

## Tratando erros

Algumas coisas dão erro e você **sabe** que podem dar: o usuário digita letra em vez de número, o arquivo não existe. Em vez de o programa quebrar, você trata:

```python
try:
    n = int(input("Número: "))
except ValueError:
    print("Isso não é um número")
```

```python
try:
    with open("dados.txt", encoding="utf-8") as f:
        texto = f.read()
except FileNotFoundError:
    texto = ""
```

Trate o erro **específico** (`ValueError`, `FileNotFoundError`) e não um `except:` genérico, que esconde outros problemas.

## JSON

JSON é um formato de texto para guardar listas e dicionários. O módulo `json` já vem com o Python:

```python
import json

dados = {"nome": "Ana", "notas": [8, 9.5]}

with open("dados.json", "w", encoding="utf-8") as f:
    json.dump(dados, f, ensure_ascii=False, indent=2)

with open("dados.json", encoding="utf-8") as f:
    lidos = json.load(f)
```

## Comparando com C

Em C você usa `fopen`, `fgets`/`fprintf` e `fclose`, e precisa verificar se o ponteiro veio `NULL`. Em Python o `with` cuida do fechamento e o `try/except` substitui as verificações manuais.

## Dicas

- Os testes deste módulo criam arquivos temporários sozinhos. Você não precisa criar nada.
- As funções recebem o **caminho** do arquivo como parâmetro (não escreva um nome fixo dentro delas).


---

## Exercícios

### Exercício 01: Ler linhas de um arquivo

Escreva `ler_linhas(caminho)` que devolve uma lista com as linhas do arquivo, sem o `\n` do final. Um arquivo vazio devolve `[]`.

Arquivo: `exercicio_01.py`  
Teste: `pytest 06-arquivos-e-erros -k exercicio_01`

### Exercício 02: Contar linhas

Escreva `contar_linhas(caminho)` que devolve quantas linhas o arquivo tem.

Arquivo: `exercicio_02.py`  
Teste: `pytest 06-arquivos-e-erros -k exercicio_02`

### Exercício 03: Salvar uma lista em arquivo

Escreva `salvar_lista(caminho, itens)` que grava cada item da lista em uma linha do arquivo, apagando o que existia antes. Os itens podem ser números, então converta com `str()`.

Arquivo: `exercicio_03.py`  
Teste: `pytest 06-arquivos-e-erros -k exercicio_03`

### Exercício 04: Converter para inteiro com segurança

Escreva `ler_inteiro_seguro(texto)` que tenta converter o texto em inteiro e devolve o número. Se não der, devolve `None` (use `try/except ValueError`).

Arquivo: `exercicio_04.py`  
Teste: `pytest 06-arquivos-e-erros -k exercicio_04`

### Exercício 05: Somar os números de um arquivo

Escreva `somar_arquivo(caminho)`. O arquivo tem um valor por linha. Some todos os valores que forem números (inteiros ou decimais), **ignorando** linhas vazias ou com texto. Devolva a soma como `float`. Se o arquivo não existir, devolva `0`.

Arquivo: `exercicio_05.py`  
Teste: `pytest 06-arquivos-e-erros -k exercicio_05`

### Exercício 06: Salvar e carregar JSON

Escreva duas funções: `salvar_json(caminho, dados)`, que grava os dados em JSON, e `carregar_json(caminho, padrao)`, que lê o JSON e devolve os dados. Se o arquivo não existir **ou** estiver com JSON inválido, devolva o valor de `padrao`. Use `encoding="utf-8"` e `ensure_ascii=False`.

Arquivo: `exercicio_06.py`  
Teste: `pytest 06-arquivos-e-erros -k exercicio_06`

---

## Rodando os testes

```bash
pytest 06-arquivos-e-erros             # todos os exercícios deste módulo
pytest 06-arquivos-e-erros -k exercicio_03   # só o exercício 03
```

Um teste que passa mostra um ponto (`.`) e um que falha mostra um `F` com a explicação do que foi esperado e do que o seu programa fez. Leia essa mensagem com calma, ela costuma dizer exatamente onde está o problema.

## Ao terminar o módulo

1. Confira se todos os testes passam.
2. Faça o commit na sua branch e abra um pull request pedindo a revisão do Pedro (veja `docs/git-e-github.md`).
3. Marque o módulo como concluído no `README.md` da raiz.
