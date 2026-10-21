# Módulo 03: Repetição: laços while e for

## O que você vai aprender

- `while` e `for`
- `range`
- `break` e `continue`
- O padrão do acumulador (somar, contar, multiplicar)

## while

Repete enquanto a condição for verdadeira:

```python
contador = 1
while contador <= 3:
    print(contador)
    contador += 1      # em Python não existe contador++
```

## for com range

O `for` do Python percorre uma sequência. Para repetir números, usa-se o `range`:

```python
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):       # 1, 2, 3, 4, 5  (o último não entra!)
    print(i)

for i in range(10, 0, -2):  # 10, 8, 6, 4, 2  (passo -2)
    print(i)
```

Compare com o C: `for (int i = 1; i <= 5; i++)` vira `for i in range(1, 6)`.

## O padrão do acumulador

Quase todo exercício de laço é uma variação disto: começar com um valor inicial e ir atualizando.

```python
total = 0
for i in range(1, 11):
    total += i
print(total)   # 55
```

Para somar começa em `0`. Para multiplicar (fatorial, por exemplo), começa em `1`.

## break e continue

```python
while True:                      # laço "infinito" com saída controlada
    n = int(input("Número (0 para sair): "))
    if n == 0:
        break                    # sai do laço
    if n < 0:
        continue                 # pula para a próxima volta
    print("Recebi", n)
```

## Dicas

- Se o programa travou num laço infinito, aperte `Ctrl + C`.
- Para entender o que o laço está fazendo, coloque um `print` dentro dele e acompanhe os valores.
- Um laço que lê "até aparecer 0" funciona bem com `while True` e `break`.


---

## Exercícios

### Exercício 01: Tabuada

Leia um número e mostre a tabuada dele de 1 a 10, uma linha por multiplicação, no formato `7 x 3 = 21`.

Exemplo:

```text
Entrada:
7

Saída:
7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70
```

Arquivo: `exercicio_01.py`  
Teste: `pytest 03-repeticao -k exercicio_01`

### Exercício 02: Soma de 1 até N

Leia um número `n` e mostre a soma de 1 até `n`, no formato `Soma: X`.

Exemplo:

```text
Entrada:
10

Saída:
Soma: 55
```

Arquivo: `exercicio_02.py`  
Teste: `pytest 03-repeticao -k exercicio_02`

### Exercício 03: Fatorial

Leia um número inteiro `n >= 0` e mostre o fatorial no formato `Fatorial: X`. Lembre que o fatorial de 0 é 1.

Exemplo:

```text
Entrada:
5

Saída:
Fatorial: 120
```

Arquivo: `exercicio_03.py`  
Teste: `pytest 03-repeticao -k exercicio_03`

### Exercício 04: Ler até aparecer zero

Leia números, um por linha, até aparecer o `0` (o zero não conta). Ao final mostre a soma e a quantidade de números lidos, em duas linhas: `Soma: X` e `Quantidade: Y`.

Exemplo:

```text
Entrada:
3
5
2
0

Saída:
Soma: 10
Quantidade: 3
```

Arquivo: `exercicio_04.py`  
Teste: `pytest 03-repeticao -k exercicio_04`

### Exercício 05: Número primo

Leia um número inteiro maior ou igual a 2 e mostre `primo` ou `composto`. Dica: tente dividir por todos os números de 2 até `n - 1` (depois você pode pensar em como fazer menos testes).

Exemplo:

```text
Entrada:
7

Saída:
primo
```

Arquivo: `exercicio_05.py`  
Teste: `pytest 03-repeticao -k exercicio_05`

### Exercício 06: Sequência de Fibonacci

Leia `n` (pelo menos 1) e mostre os `n` primeiros termos da sequência de Fibonacci, separados por espaço, em uma única linha. A sequência começa com `0 1` e cada termo seguinte é a soma dos dois anteriores. Dica: `print(a, end=" ")` não pula linha.

Exemplo:

```text
Entrada:
8

Saída:
0 1 1 2 3 5 8 13
```

Arquivo: `exercicio_06.py`  
Teste: `pytest 03-repeticao -k exercicio_06`

---

## Rodando os testes

```bash
pytest 03-repeticao             # todos os exercícios deste módulo
pytest 03-repeticao -k exercicio_03   # só o exercício 03
```

Um teste que passa mostra um ponto (`.`) e um que falha mostra um `F` com a explicação do que foi esperado e do que o seu programa fez. Leia essa mensagem com calma, ela costuma dizer exatamente onde está o problema.

## Ao terminar o módulo

1. Confira se todos os testes passam.
2. Faça o commit na sua branch e abra um pull request pedindo a revisão do Pedro (veja `docs/git-e-github.md`).
3. Marque o módulo como concluído no `README.md` da raiz.
