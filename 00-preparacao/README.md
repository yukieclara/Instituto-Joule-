# Módulo 00: Preparação

Antes dos exercícios, vamos deixar o computador pronto. Reserve uns 30 minutos.

## 1. Instalar o Python

1. Acesse [python.org/downloads](https://www.python.org/downloads/) e baixe a versão mais recente.
2. No Windows, **marque a opção "Add Python to PATH"** na primeira tela do instalador. Isso é importante.
3. Para conferir, abra o terminal (no Windows, procure por "Prompt de Comando" ou "PowerShell") e digite:

```bash
python --version
```

Deve aparecer algo como `Python 3.12.x`. Em alguns computadores (Mac e Linux) o comando é `python3`.

## 2. Instalar o VS Code

Baixe em [code.visualstudio.com](https://code.visualstudio.com/). Dentro dele, instale a extensão **Python** (da Microsoft) pela aba de extensões.

## 3. Instalar o Git e criar a conta no GitHub

- Git: [git-scm.com](https://git-scm.com/downloads). Pode deixar as opções padrão.
- GitHub: crie a conta em [github.com](https://github.com). Escolha um nome de usuário profissional, de preferência com o seu nome, porque ele vai aparecer no currículo.

Confirme que o Git funciona:

```bash
git --version
```

## 4. Rodar o primeiro programa

Com a sua cópia do repositório aberta no VS Code, abra o terminal do VS Code (menu Terminal, depois New Terminal) e rode:

```bash
python 00-preparacao/ola_mundo.py
```

Se aparecer `Olá, mundo!`, está tudo certo.

## 5. Instalar o pytest

```bash
pip install -r requirements.txt
```

Para confirmar:

```bash
pytest --version
```

## Se algo der errado

- `python` não é reconhecido: no Windows, reinstale o Python marcando "Add Python to PATH". No Mac/Linux, tente `python3`.
- `pip` não é reconhecido: tente `python -m pip install -r requirements.txt`.
- Qualquer outro erro: copie a mensagem inteira e mande para o mentor. Erro de instalação é muito comum e geralmente se resolve rápido.

## Quando terminar

Marque a preparação como concluída no `README.md` da raiz e siga para o módulo 01.
