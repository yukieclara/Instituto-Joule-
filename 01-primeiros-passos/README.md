# Módulo 01: Primeiros passos: variáveis, entrada e saída

## O que você vai aprender

- Mostrar coisas na tela com `print`
- Guardar valores em variáveis (sem declarar o tipo)
- Ler o que a pessoa digita com `input`
- Fazer contas com os operadores

## Mostrando e guardando

```python
nome = "Ana"
idade = 18
print("Oi,", nome)
print(f"{nome} tem {idade} anos")   # f-string: o jeito mais prático de montar textos
```

Em Python você não escreve o tipo da variável. Ela assume o tipo do valor que recebe: `int` (inteiro), `float` (decimal), `str` (texto) e `bool` (`True` ou `False`). Para ver o tipo, use `type(idade)`.

## Lendo dados do teclado

```python
nome = input("Qual é o seu nome? ")
print(f"Olá, {nome}!")
```

**Atenção:** o `input` sempre devolve texto. Se você quer fazer conta, precisa converter:

```python
a = int(input("Primeiro número: "))     # inteiro
b = float(input("Segundo número: "))    # decimal
print(a + b)
```

## Operadores

| Operação | Símbolo | Exemplo | Resultado |
|---|---|---|---|
| Soma, subtração, multiplicação | `+ - *` | `3 * 4` | `12` |
| Divisão (sempre decimal) | `/` | `7 / 2` | `3.5` |
| Divisão inteira | `//` | `7 // 2` | `3` |
| Resto da divisão | `%` | `7 % 2` | `1` |
| Potência | `**` | `2 ** 10` | `1024` |

## Formatando números

Dentro da f-string, `:.2f` mostra 2 casas decimais:

```python
media = 8.0
print(f"Média: {media:.2f}")   # Média: 8.00
```

## Comparando com C

| C | Python |
|---|---|
| `int x = 5;` | `x = 5` |
| `printf("%d\n", x);` | `print(x)` |
| `scanf("%d", &x);` | `x = int(input())` |
| `x / y` com inteiros dá divisão inteira | `x / y` é sempre decimal; use `//` para a inteira |

## Antes de começar os exercícios

- Cada exercício tem um arquivo `exercicio_XX.py` com um comentário dizendo o que fazer. Escreva o seu código nele.
- Mantenha **exatamente** o formato de saída pedido (por exemplo, `Soma: 7`). O teste procura esse texto.
- Você pode colocar uma mensagem no `input`, como `input("Digite um número: ")`. Isso não atrapalha o teste.


---

## Exercícios

### Exercício 01: Olá, mundo personalizado

Peça o nome da pessoa e mostre `Olá, <nome>!`.

Exemplo:

```text
Entrada:
Ana

Saída:
Olá, Ana!
```

Arquivo: `exercicio_01.py`  
Teste: `pytest 01-primeiros-passos -k exercicio_01`

### Exercício 02: Soma de dois números

Leia dois números inteiros e mostre a soma no formato `Soma: X`.

Exemplo:

```text
Entrada:
3
4

Saída:
Soma: 7
```

Arquivo: `exercicio_02.py`  
Teste: `pytest 01-primeiros-passos -k exercicio_02`

### Exercício 03: Média de três notas

Leia três notas (use ponto como separador decimal, como `7.5`) e mostre a média com 2 casas decimais, no formato `Média: X.XX`.

Exemplo:

```text
Entrada:
7
8
9

Saída:
Média: 8.00
```

Arquivo: `exercicio_03.py`  
Teste: `pytest 01-primeiros-passos -k exercicio_03`

### Exercício 04: Celsius para Fahrenheit

Leia uma temperatura em graus Celsius e mostre em Fahrenheit com 1 casa decimal, no formato `Fahrenheit: X.X`. A fórmula é `F = C * 9 / 5 + 32`.

Exemplo:

```text
Entrada:
100

Saída:
Fahrenheit: 212.0
```

Arquivo: `exercicio_04.py`  
Teste: `pytest 01-primeiros-passos -k exercicio_04`

### Exercício 05: Quociente e resto

Leia dois inteiros `a` e `b` e mostre, em duas linhas, o quociente inteiro e o resto da divisão de `a` por `b`, nos formatos `Quociente: X` e `Resto: Y`.

Exemplo:

```text
Entrada:
17
5

Saída:
Quociente: 3
Resto: 2
```

Arquivo: `exercicio_05.py`  
Teste: `pytest 01-primeiros-passos -k exercicio_05`

### Exercício 06: Segundos em horas, minutos e segundos

Leia uma quantidade de segundos e mostre no formato `Tempo: H:MM:SS`, com minutos e segundos sempre com 2 dígitos. Dica: use `//` e `%`, e `:02d` dentro da f-string.

Exemplo:

```text
Entrada:
3725

Saída:
Tempo: 1:02:05
```

Arquivo: `exercicio_06.py`  
Teste: `pytest 01-primeiros-passos -k exercicio_06`

---

## Rodando os testes

```bash
pytest 01-primeiros-passos             # todos os exercícios deste módulo
pytest 01-primeiros-passos -k exercicio_03   # só o exercício 03
```

Um teste que passa mostra um ponto (`.`) e um que falha mostra um `F` com a explicação do que foi esperado e do que o seu programa fez. Leia essa mensagem com calma, ela costuma dizer exatamente onde está o problema.

## Ao terminar o módulo

1. Confira se todos os testes passam.
2. Faça o commit na sua branch e abra um pull request pedindo a revisão do Pedro (veja `docs/git-e-github.md`).
3. Marque o módulo como concluído no `README.md` da raiz.
