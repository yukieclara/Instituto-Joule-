# Comparando C e Python

Se você já viu C, boa parte do que vem aí vai ser familiar. Aqui está um mapa para você se orientar.

## Visão geral

| | C | Python |
|---|---|---|
| Tipo de variável | declarado (`int x;`) | automático (`x = 5`) |
| Compilação | compila e depois executa | interpretado: roda direto |
| Blocos de código | chaves `{ }` | indentação e `:` |
| Fim de instrução | `;` | quebra de linha |
| Memória | você gerencia (`malloc`, `free`) | automática |
| Vetores | tamanho fixo | listas que crescem sozinhas |
| Texto | vetor de `char` com `\0` | tipo `str` pronto |

## Mesmo programa nas duas linguagens

Ler dois números e mostrar a soma:

```c
#include <stdio.h>

int main(void) {
    int a, b;
    scanf("%d", &a);
    scanf("%d", &b);
    printf("Soma: %d\n", a + b);
    return 0;
}
```

```python
a = int(input())
b = int(input())
print(f"Soma: {a + b}")
```

## Decisões e repetições

```c
if (nota >= 7) {
    printf("aprovado\n");
} else if (nota >= 5) {
    printf("recuperacao\n");
} else {
    printf("reprovado\n");
}

for (int i = 1; i <= 5; i++) {
    printf("%d\n", i);
}
```

```python
if nota >= 7:
    print("aprovado")
elif nota >= 5:
    print("recuperacao")
else:
    print("reprovado")

for i in range(1, 6):
    print(i)
```

## Vetor e lista

```c
int v[3] = {4, 8, 15};
int soma = 0;
for (int i = 0; i < 3; i++) {
    soma += v[i];
}
```

```python
v = [4, 8, 15]
soma = sum(v)
v.append(16)   # em C isso exigiria realocar memória
```

## Funções

```c
int dobro(int n) {
    return n * 2;
}
```

```python
def dobro(n):
    return n * 2
```

## O que é conceito e o que é sintaxe

Variáveis, condições, laços, funções, listas, arquivos e a forma de **pensar um problema em passos** são conceitos. Eles valem para C, Python, Java, JavaScript e o resto. O que muda é como escrever. Por isso, tudo que você aprendeu em C continua valendo: você só está aprendendo a "falar" a mesma coisa em outra língua.

## Quando usar cada uma

- **C:** quando precisa de desempenho e controle do hardware (sistemas embarcados, sistemas operacionais, drivers). É ótima para entender como as coisas funcionam por baixo.
- **Python:** quando precisa de produtividade (dados, IA, automação, scripts, protótipos, web). É onde você escreve mais rápido e tem uma biblioteca para quase tudo.

Boa parte dos profissionais usa as duas ao longo da carreira.
