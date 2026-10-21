# Módulo 05: Funções: organizando o código

## O que você vai aprender

- Criar funções com `def`
- Parâmetros e retorno (`return`)
- A diferença entre `print` e `return`
- Como o teste automático "enxerga" a sua função

## Criando uma função

```python
def area_quadrado(lado):
    return lado * lado

resultado = area_quadrado(4)
print(resultado)    # 16
```

Em C você escreveria o tipo do retorno e dos parâmetros (`int area(int lado)`). Em Python não precisa: a função aceita o que você passar e devolve o que você mandar no `return`.

## print não é return

Esta é a confusão mais comum de quem está começando:

```python
def dobro_errado(n):
    print(n * 2)       # só mostra na tela. A função devolve None.

def dobro_certo(n):
    return n * 2       # devolve o valor para quem chamou

x = dobro_certo(5) + 1     # 11
```

`return` **devolve** o valor e encerra a função. Quem chamou pode guardar, somar, comparar. Já o `print` só mostra na tela.

## Valores padrão e vários retornos

```python
def saudacao(nome, cumprimento="Olá"):
    return f"{cumprimento}, {nome}!"

print(saudacao("Ana"))                 # Olá, Ana!
print(saudacao("Ana", "Bom dia"))      # Bom dia, Ana!

def min_e_max(lista):
    return min(lista), max(lista)      # devolve dois valores de uma vez

menor, maior = min_e_max([3, 1, 9])
```

## Escopo

Variáveis criadas dentro da função existem **só dentro dela**. Se precisa de um valor lá dentro, receba como parâmetro.

## Como os testes funcionam neste módulo

Nos módulos anteriores o teste rodava o seu programa inteiro. Agora o teste **chama a sua função** com valores e confere o que ela devolve. Por isso:

- Escreva a função com **o nome e os parâmetros exatamente como estão no arquivo inicial**.
- Use `return`. Se a função só imprimir, o teste vai ver `None`.
- Não deixe `input()` solto no arquivo (fora de função), senão o teste trava esperando você digitar.
- Se quiser testar na mão, crie no fim do arquivo:

```python
if __name__ == "__main__":
    print(eh_primo(7))
```

O bloco `if __name__ == "__main__":` só roda quando você executa o arquivo direto, e não quando o teste importa.

## Dicas

- Funções pequenas, que fazem uma coisa só, são mais fáceis de testar e de entender.
- Use o `pytest -k exercicio_03` para rodar só um exercício e ler a mensagem de erro com calma.


---

## Exercícios

### Exercício 01: Área do retângulo

Escreva `area_retangulo(base, altura)` que devolve a área.

Arquivo: `exercicio_01.py`  
Teste: `pytest 05-funcoes -k exercicio_01`

### Exercício 02: É primo?

Escreva `eh_primo(n)` que devolve `True` se `n` for primo e `False` caso contrário. Lembre que 0 e 1 não são primos.

Arquivo: `exercicio_02.py`  
Teste: `pytest 05-funcoes -k exercicio_02`

### Exercício 03: Maior elemento

Escreva `maior_elemento(lista)` que devolve o maior número da lista, **sem usar a função `max`**. Considere que a lista tem pelo menos um elemento.

Arquivo: `exercicio_03.py`  
Teste: `pytest 05-funcoes -k exercicio_03`

### Exercício 04: Contar palavras

Escreva `contar_palavras(texto)` que devolve quantas palavras o texto tem. Espaços a mais no começo, no fim ou no meio não contam. Dica: `split()` sem argumentos já resolve isso.

Arquivo: `exercicio_04.py`  
Teste: `pytest 05-funcoes -k exercicio_04`

### Exercício 05: FizzBuzz

Escreva `fizzbuzz(n)` que **devolve** (não imprime) um texto: `"FizzBuzz"` se `n` for múltiplo de 3 e de 5, `"Fizz"` se for múltiplo só de 3, `"Buzz"` se for múltiplo só de 5, ou o próprio número como texto nos outros casos (por exemplo `"7"`).

Arquivo: `exercicio_05.py`  
Teste: `pytest 05-funcoes -k exercicio_05`

### Exercício 06: Palíndromo de frase

Escreva `eh_palindromo(texto)` que devolve `True` se o texto é igual de trás para frente, **ignorando espaços e diferença entre maiúsculas e minúsculas**. Exemplo: `"Anotaram a data da maratona"` é um palíndromo.

Arquivo: `exercicio_06.py`  
Teste: `pytest 05-funcoes -k exercicio_06`

---

## Rodando os testes

```bash
pytest 05-funcoes             # todos os exercícios deste módulo
pytest 05-funcoes -k exercicio_03   # só o exercício 03
```

Um teste que passa mostra um ponto (`.`) e um que falha mostra um `F` com a explicação do que foi esperado e do que o seu programa fez. Leia essa mensagem com calma, ela costuma dizer exatamente onde está o problema.

## Ao terminar o módulo

1. Confira se todos os testes passam.
2. Faça o commit na sua branch e abra um pull request pedindo a revisão do Pedro (veja `docs/git-e-github.md`).
3. Marque o módulo como concluído no `README.md` da raiz.
