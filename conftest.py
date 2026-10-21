"""Ferramentas dos testes. Você não precisa mexer neste arquivo."""
import importlib.util
import os
import subprocess
import sys

import pytest


@pytest.fixture
def verificar(request):
    """Roda um programa com entradas simuladas e confere o que ele escreveu."""
    pasta = request.path.parent

    def _verificar(arquivo, casos):
        for entradas, deve, nao_deve in casos:
            env = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONUTF8="1")
            try:
                proc = subprocess.run(
                    [sys.executable, str(pasta / arquivo)],
                    input="\n".join(entradas) + "\n",
                    capture_output=True, text=True, encoding="utf-8",
                    timeout=5, env=env,
                )
            except subprocess.TimeoutExpired:
                pytest.fail(f"Com a entrada {entradas} o programa demorou demais (laço infinito?).", pytrace=False)
            if proc.returncode != 0:
                pytest.fail(f"Com a entrada {entradas} o programa deu erro:\n{proc.stderr}", pytrace=False)
            saida = proc.stdout
            for trecho in deve:
                if trecho not in saida:
                    pytest.fail(
                        f"\nEntrada: {entradas}\nEu esperava ver: {trecho!r}\nO seu programa mostrou:\n{saida}",
                        pytrace=False)
            for trecho in nao_deve:
                if trecho in saida:
                    pytest.fail(
                        f"\nEntrada: {entradas}\nNão era para aparecer: {trecho!r}\nO seu programa mostrou:\n{saida}",
                        pytrace=False)

    return _verificar


@pytest.fixture
def carregar(request):
    """Importa um arquivo .py da pasta do teste, para chamar as funções dele."""
    pasta = request.path.parent

    def _carregar(nome):
        spec = importlib.util.spec_from_file_location(f"{pasta.name}_{nome[:-3]}".replace("-", "_"), pasta / nome)
        modulo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(modulo)
        return modulo

    return _carregar
