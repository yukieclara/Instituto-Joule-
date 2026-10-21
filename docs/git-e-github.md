# Git e GitHub: o básico que você precisa

O Git guarda o histórico do seu código e o GitHub é o site onde ele fica online. Você não precisa saber tudo, só o fluxo abaixo.

## Configuração (só uma vez)

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu-email@exemplo.com"
```

## Pegando o repositório

Na página do repositório que você criou a partir do modelo, clique em **Code**, copie o endereço HTTPS e rode:

```bash
git clone <endereço-copiado>
cd <nome-do-repositório>
```

## O fluxo de cada módulo

1. **Crie uma branch** (uma "linha de trabalho" separada) para o módulo:

```bash
git checkout -b modulo-01
```

2. **Faça os exercícios.** De vez em quando, salve o progresso:

```bash
git add .
git commit -m "Resolve exercícios 01 a 03 do módulo 01"
```

Escreva mensagens que digam o que você fez. Fazer commits pequenos e frequentes é um bom hábito.

3. **Envie para o GitHub:**

```bash
git push -u origin modulo-01
```

4. **Abra um pull request:** no GitHub vai aparecer um botão **Compare & pull request**. Clique, escreva um resumo do que fez (e as dúvidas que ficaram) e peça a revisão do mentor em **Reviewers**.

5. **Leia os comentários**, faça os ajustes na mesma branch (`add`, `commit`, `push` de novo) e, quando o mentor aprovar, clique em **Merge pull request**.

6. **Volte para a principal e atualize:**

```bash
git checkout main
git pull
```

E recomece com a branch do próximo módulo.

## Comandos úteis

| Comando | Para que serve |
|---|---|
| `git status` | Mostra o que mudou |
| `git log --oneline` | Mostra o histórico resumido |
| `git diff` | Mostra as mudanças ainda não salvas |
| `git checkout -b nome` | Cria e entra em uma branch nova |
| `git checkout nome` | Troca de branch |

## Se algo der errado

- Não entre em pânico. Quase tudo no Git tem conserto. Antes de tentar comandos que você não conhece, **mande a mensagem de erro para o mentor**.
- Se o Git pedir login ao enviar, siga as instruções que aparecem na tela para autorizar a sua conta do GitHub.
- Não coloque no repositório senhas, chaves ou documentos pessoais. Se colocar sem querer, avise na hora, porque só apagar o arquivo não remove do histórico.
