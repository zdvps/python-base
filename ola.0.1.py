#!/usr/bin/env python3
# Atualizado: 10/03/25
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
__version__ = "0.1.2"
__author__ = "Zenio Almeida - zn-dv@outlook.com"
__license__  = "Unlicense"
# dunder é __ 2 underlines

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = {
  "en_US": "Hello, I'm Zenio Working with AIOps Enginner",
  "pt_BR": "Olá, sou Zenio Trabalho com AIOps Enginner",
  "es_SP": "Hola, soy Zenio trabajando con AIOps Enginner",
}

print(msg[current_language])

