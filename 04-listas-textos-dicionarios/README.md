# Módulo 04: Listas, textos e dicionários

## O que você vai aprender

- Listas (o "vetor" do Python, só que muito mais flexível)
- Textos (`str`) e seus métodos
- Dicionários (guardar pares chave e valor)

## Listas

```python
numeros = [4, 8, 15]
numeros.append(16)          # adiciona no fim
print(numeros[0])           # 4 (índice começa em 0)
print(numeros[-1])          # 16 (o último)
print(len(numeros))         # 4

for n in numeros:           # percorre os elementos direto
    print(n)

print(sum(numeros), min(numeros), max(numeros))
```

Diferenças importantes em relação aos vetores do C: a lista cresce sozinha, aceita qualquer tipo, e você não precisa controlar o tamanho nem lidar com memória.

## Fatiamento (slicing)

```python
letras = [10, 20, 30, 40, 50]
print(letras[1:4])    # [20, 30, 40]  (do 1 até antes do 4)
print(letras[:2])     # [10, 20]
print(letras[::-1])   # [50, 40, 30, 20, 10]  (invertida)
```

## Textos

Um texto funciona como uma lista de caracteres, e o fatiamento também funciona nele:

```python
texto = "Python"
print(texto[0])        # P
print(texto[::-1])     # nohtyP
print(texto.lower())   # python
print(texto.upper())   # PYTHON
print(len(texto))      # 6
```

Textos **não podem ser alterados** no lugar: métodos como `lower()` devolvem um texto novo. Para quebrar e juntar:

```python
palavras = "um dois três".split()     # ['um', 'dois', 'três']
frase = " ".join(palavras)            # 'um dois três'
```

E para saber se um item está em uma lista ou texto, use `in`:

```python
if "a" in "banana":
    print("tem a")
```

## Dicionários

Associam uma chave a um valor:

```python
idades = {"Ana": 18, "Bruno": 20}
idades["Carla"] = 19               # adiciona
print(idades["Ana"])               # 18

for nome, idade in idades.items():
    print(f"{nome}: {idade}")

contagem = {}
contagem["a"] = contagem.get("a", 0) + 1   # .get devolve 0 se a chave não existir
```

O `.get(chave, padrão)` é muito útil para contar coisas.

## Dicas

- Transforme em minúsculas (`lower()`) antes de comparar textos, para não diferenciar maiúscula de minúscula.
- O `input().split()` lê uma linha com vários valores separados por espaço.
- Se precisar converter uma lista de textos em inteiros: `[int(x) for x in partes]`.


---

## Exercícios

### Exercício 01: Maior e menor de uma lista

Leia 5 números inteiros (um por linha), guarde em uma lista e mostre o maior e o menor em duas linhas: `Maior: X` e `Menor: Y`.

Exemplo:

```text
Entrada:
3
9
1
7
5

Saída:
Maior: 9
Menor: 1
```

Arquivo: `exercicio_01.py`  
Teste: `pytest 04-listas-textos-dicionarios -k exercicio_01`

### Exercício 02: Texto invertido

Leia um texto e mostre ele de trás para frente. Use fatiamento.

Exemplo:

```text
Entrada:
python

Saída:
nohtyp
```

Arquivo: `exercicio_02.py`  
Teste: `pytest 04-listas-textos-dicionarios -k exercicio_02`

### Exercício 03: Contar vogais

Leia um texto e conte quantas vogais (`a`, `e`, `i`, `o`, `u`, maiúsculas ou minúsculas, sem considerar acentos) ele tem. Mostre `Vogais: X`.

Exemplo:

```text
Entrada:
Programacao

Saída:
Vogais: 5
```

Arquivo: `exercicio_03.py`  
Teste: `pytest 04-listas-textos-dicionarios -k exercicio_03`

### Exercício 04: Palíndromo

Leia uma palavra e mostre `sim` se ela é igual de trás para frente (um palíndromo), ou `nao` caso contrário. Não diferencie maiúsculas de minúsculas.

Exemplo:

```text
Entrada:
arara

Saída:
sim
```

Arquivo: `exercicio_04.py`  
Teste: `pytest 04-listas-textos-dicionarios -k exercicio_04`

### Exercício 05: Frequência de palavras

Leia uma frase e conte quantas vezes cada palavra aparece (sem diferenciar maiúsculas de minúsculas). Mostre uma linha por palavra no formato `palavra: quantidade`, em qualquer ordem. Use um dicionário.

Exemplo:

```text
Entrada:
a casa e a porta

Saída:
a: 2
casa: 1
e: 1
porta: 1
```

Arquivo: `exercicio_05.py`  
Teste: `pytest 04-listas-textos-dicionarios -k exercicio_05`

### Exercício 06: Remover duplicados

Leia uma linha com números inteiros separados por espaço e mostre os números sem repetição, mantendo a ordem em que apareceram, separados por espaço, em uma linha.

Exemplo:

```text
Entrada:
1 2 2 3 1

Saída:
1 2 3
```

Arquivo: `exercicio_06.py`  
Teste: `pytest 04-listas-textos-dicionarios -k exercicio_06`

---

## Rodando os testes

```bash
pytest 04-listas-textos-dicionarios             # todos os exercícios deste módulo
pytest 04-listas-textos-dicionarios -k exercicio_03   # só o exercício 03
```

Um teste que passa mostra um ponto (`.`) e um que falha mostra um `F` com a explicação do que foi esperado e do que o seu programa fez. Leia essa mensagem com calma, ela costuma dizer exatamente onde está o problema.

## Ao terminar o módulo

1. Confira se todos os testes passam.
2. Faça o commit na sua branch e abra um pull request pedindo a revisão do Pedro (veja `docs/git-e-github.md`).
3. Marque o módulo como concluído no `README.md` da raiz.
