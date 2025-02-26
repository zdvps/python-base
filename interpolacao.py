#!/usr/bin/env python3
# ----------------------
# ---- Autor: Zenio zndv@outlook.com 21977036020
# ---- Última atualização: 25/02/25

clientes = ["Maria", "Zenio", "Bruno"]

email_tmpl = """
Olá, %(nome)s
Tem interesse em comprar %(produto)s?
Este produto é ótimo para resolver
%(texto)s

Clique agora em %(link)s

Apenas %(quantidade)d disponíveis!

Preço promocional %(preco).2f
"""

for cliente in clientes:
    print(email_tmpl % {
        "nome": cliente,
        "produto": "caneta",
        "texto": "Escreve muito bem",
        "link": "https://canetaslegais.com",
        "quantidade": 1,
        "preco": 50.5
    })

