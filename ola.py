#!/usr/bin/env python3
"""
Hello Multi Languages; Ola Multi Linguas

Dependendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente.
Usage:
    Make sure the LANG variable is properly configured;;
    tenha a variável LANG devidamente configurada ex:
    export LANG=pt_BR
Execution;; Execução:
    python3 ola.py ou . ola.py
"""
__version__ = "0.0.1"
__author__ = "Zenio Almeida - zn-dv@outlook.com"
__license__  = "Unlicense"
# dunder é __ 2 underlines

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello, I'm Zenio DevOps" 
if current_language == "pt_BR":
    msg = "Olá, eu sou o Zenio DevOps"
elif current_language == "es_SP":
    msg = "Hola, soy Zenio DevOps."

print(msg)  # Corrigido o erro de indentação

