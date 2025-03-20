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
    Ou informe através do CLI argument '--lang'

    Ou o usuário terá que digitar

"""
__version__ = "0.1.3"
__author__ = "Zenio Almeida - zn-dv@outlook.com"
__license__  = "Unlicense"
# dunder é __ 2 underlines

import os
import sys

arguments = {"lang": None, "count": 1}

for arg in sys.argv[1:]:
    # TODO: Tratar ValueError
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option '{key}'")
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    # TODO: Usar repetição
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language:")

current_language = current_language[:5]

msg = {
  "en_US": "Hello, I'm Zenio Working with AIOps Enginner",
  "pt_BR": "Olá, sou Zenio Trabalho com AIOps Enginner",
  "es_SP": "Hola, soy Zenio trabajando con AIOps Enginner",
}

print(
        msg[current_language] * int(arguments["count"])
)

