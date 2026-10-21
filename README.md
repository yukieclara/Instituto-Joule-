# Trilha de Python para iniciantes

Uma sequência de módulos com **tutorial, lista de exercícios e testes automáticos**, terminando em um projeto. A ideia é você aprender praticando, no seu ritmo, e ter tudo registrado no GitHub.

Se você já programou um pouco em C, ótimo: boa parte da lógica é a mesma. O que muda é a sintaxe, e o Python deixa tudo mais curto. Tem uma comparação lado a lado em [`docs/comparando-c-e-python.md`](docs/comparando-c-e-python.md).

## Por que Python?

C é excelente para entender como o computador funciona, mas no dia a dia da maioria das áreas de tecnologia (dados, IA, automação, web, segurança) o Python aparece muito mais. Aprender a **mesma lógica** em uma segunda linguagem também mostra o que é conceito (que vale para qualquer linguagem) e o que é só sintaxe.

## O caminho

Siga a ordem, mas sem pressa. Cada pasta tem um `README.md` que funciona como tutorial: leia primeiro, depois faça os exercícios.

| Pasta | Assunto | Exercícios |
|---|---|---|
| [`00-preparacao`](00-preparacao/README.md) | Instalar o que precisa e rodar o primeiro programa | sem teste |
| [`01-primeiros-passos`](01-primeiros-passos/README.md) | Variáveis, entrada, saída e operadores | 6 |
| [`02-condicionais`](02-condicionais/README.md) | `if`, `elif`, `else` | 6 |
| [`03-repeticao`](03-repeticao/README.md) | `while`, `for`, `range` | 6 |
| [`04-listas-textos-dicionarios`](04-listas-textos-dicionarios/README.md) | Listas, textos e dicionários | 6 |
| [`05-funcoes`](05-funcoes/README.md) | Funções, parâmetros e `return` | 6 |
| [`06-arquivos-e-erros`](06-arquivos-e-erros/README.md) | Arquivos, `try/except` e JSON | 6 |
| [`07-projeto-tarefas`](07-projeto-tarefas/README.md) | Projeto: gerenciador de tarefas no terminal | 5 etapas |

Estimativa: de 1 a 2 semanas por módulo, com 3 a 4 horas por semana. Se já souber o assunto, passe rápido. Se travar, não tem problema, é para isso que o mentor está junto.

## Como trabalhar

1. **Faça a sua cópia.** Clique em **Use this template** na página do repositório e crie o repositório na sua conta, com o nome que quiser. Assim ele fica no seu perfil.
2. **Convide o mentor** como colaborador (Settings, depois Collaborators).
3. **Clone** para o seu computador e abra no VS Code (passo a passo em [`docs/git-e-github.md`](docs/git-e-github.md)).
4. **Um módulo por vez:** leia o `README.md` da pasta, faça os exercícios editando os arquivos `exercicio_XX.py` e rode os testes.
5. **Entregue por pull request:** cada módulo em uma branch (`modulo-01`, `modulo-02`...). Quando terminar, abra um pull request e peça a revisão. O mentor comenta e sugere melhorias, e você ajusta.

## Rodando os testes

Na primeira vez, instale o pytest:

```bash
pip install -r requirements.txt
```

Depois, na pasta do repositório:

```bash
pytest 01-primeiros-passos          # testa um módulo
pytest 01-primeiros-passos -k exercicio_02   # testa só um exercício
```

No começo **todos os testes falham**, e isso é esperado: você ainda não resolveu nada. O objetivo é ir deixando-os verdes.

## Regras do jogo

- **Você escreve o código.** Pode (e deve) consultar documentação, tutoriais e colegas.
- **Usar IA é permitido para entender, não para copiar.** Peça que ela explique um erro ou um conceito, mas não cole a resposta pronta. Regra de ouro: só entregue o que você consegue explicar com as suas palavras. No pull request, o mentor pode pedir que você explique um trecho.
- **Errar faz parte.** Teste que falha é informação, não bronca.
- **Não publique** senhas, chaves, documentos nem dados pessoais no repositório.

## Seu progresso

- [ ] 00 Preparação
- [ ] 01 Primeiros passos
- [ ] 02 Condicionais
- [ ] 03 Repetição
- [ ] 04 Listas, textos e dicionários
- [ ] 05 Funções
- [ ] 06 Arquivos e erros
- [ ] 07 Projeto: gerenciador de tarefas

## Depois da trilha

Quando terminar, você terá um repositório com 36 exercícios resolvidos e um projeto completo, pronto para entrar no currículo e no LinkedIn. Vale também refazer partes em C para comparar, ou pensar em um projeto seu usando o que aprendeu.
