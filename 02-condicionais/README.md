# Módulo 02: Condicionais: tomando decisões

## O que você vai aprender

- `if`, `elif` e `else`
- Operadores de comparação e lógicos
- A regra da indentação (o espaço no começo da linha)

## Estrutura básica

```python
nota = float(input("Nota: "))

if nota >= 7:
    print("aprovado")
elif nota >= 5:
    print("recuperacao")
else:
    print("reprovado")
```

Repare em três diferenças em relação ao C:

1. Não tem chaves `{}`. Quem define o bloco é a **indentação** (4 espaços). O `:` no fim da linha é obrigatório.
2. Não precisa de parênteses em volta da condição.
3. É `elif`, e não `else if`.

## Comparações e lógica

| Ideia | Python |
|---|---|
| igual / diferente | `==` e `!=` |
| maior, menor | `>` `<` `>=` `<=` |
| e, ou, não | `and`, `or`, `not` (em C: `&&`, `||`, `!`) |

```python
idade = 20
if idade >= 18 and idade < 60:
    print("adulto")
```

Em Python dá até para escrever `18 <= idade < 60`.

## Cuidados comuns

- `=` guarda um valor, `==` compara. Trocar um pelo outro é o erro clássico.
- Comparar texto com `==` funciona (`if op == "+":`), e diferencia maiúscula de minúscula.
- A ordem do `if/elif` importa: o Python para no primeiro que for verdadeiro.

## Dica para os exercícios

Antes de programar, escreva no papel os casos de teste, incluindo os de borda (o valor exato em que a decisão muda, como a nota 7 ou o ano 2000).


---

## Exercícios

### Exercício 01: Par ou ímpar

Leia um número inteiro e mostre `par` ou `impar` (sem acento).

Exemplo:

```text
Entrada:
7

Saída:
impar
```

Arquivo: `exercicio_01.py`  
Teste: `pytest 02-condicionais -k exercicio_01`

### Exercício 02: Maior de três

Leia três números inteiros e mostre o maior no formato `Maior: X`. Tente resolver com `if`, sem usar a função `max`.

Exemplo:

```text
Entrada:
1
5
3

Saída:
Maior: 5
```

Arquivo: `exercicio_02.py`  
Teste: `pytest 02-condicionais -k exercicio_02`

### Exercício 03: Aprovado, recuperação ou reprovado

Leia a média de um aluno (número com ponto decimal). Mostre `aprovado` se for 7 ou mais, `recuperacao` se for de 5 até menos de 7, e `reprovado` se for menor que 5. Sem acentos.

Exemplo:

```text
Entrada:
6.5

Saída:
recuperacao
```

Arquivo: `exercicio_03.py`  
Teste: `pytest 02-condicionais -k exercicio_03`

### Exercício 04: Ano bissexto

Leia um ano e mostre `bissexto` ou `comum`. Um ano é bissexto se for divisível por 4 e não por 100, ou se for divisível por 400.

Exemplo:

```text
Entrada:
2024

Saída:
bissexto
```

Arquivo: `exercicio_04.py`  
Teste: `pytest 02-condicionais -k exercicio_04`

### Exercício 05: Tipo de triângulo

Leia os três lados de um triângulo e mostre `invalido` se não formar um triângulo (cada lado precisa ser menor que a soma dos outros dois), ou `equilatero` (3 lados iguais), `isosceles` (2 iguais) ou `escaleno` (todos diferentes). Sem acentos.

Exemplo:

```text
Entrada:
3
4
5

Saída:
escaleno
```

Arquivo: `exercicio_05.py`  
Teste: `pytest 02-condicionais -k exercicio_05`

### Exercício 06: Calculadora simples

Leia um número, uma operação (`+`, `-`, `*` ou `/`) e outro número, nessa ordem, cada um em uma linha. Mostre `Resultado: X` (como número decimal, por exemplo `42.0`). Se for divisão por zero ou uma operação desconhecida, mostre `Erro`.

Exemplo:

```text
Entrada:
6
*
7

Saída:
Resultado: 42.0
```

Arquivo: `exercicio_06.py`  
Teste: `pytest 02-condicionais -k exercicio_06`

---

## Rodando os testes

```bash
pytest 02-condicionais             # todos os exercícios deste módulo
pytest 02-condicionais -k exercicio_03   # só o exercício 03
```

Um teste que passa mostra um ponto (`.`) e um que falha mostra um `F` com a explicação do que foi esperado e do que o seu programa fez. Leia essa mensagem com calma, ela costuma dizer exatamente onde está o problema.

## Ao terminar o módulo

1. Confira se todos os testes passam.
2. Faça o commit na sua branch e abra um pull request pedindo a revisão do Pedro (veja `docs/git-e-github.md`).
3. Marque o módulo como concluído no `README.md` da raiz.
