#!/usr/bin/env python3
"""Imprime a tabuada do 1 ao 10.

----Tabuada do 1----

    1 x 1 = 1
    2 x 1 = 2
    3 x 1 = 3
.....
###################
----Tabuada do 2----

    2 x 1 = 2
    2 x 2 = 4 
    4 x 4 = 8
......
###################
"""
__version__ = "0.1.0"
__author__ = "Zenio"
# Atualização : 27/02/25

template = """
 ----Tabuada do 2----
{bloco:^18}

###################
"""

# Iterable (percorriveis)
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = list(range(1, 11))
# para cada numero em numeros:

for n1 in numeros:
    print("{:-^18}".format(f"Tabuada do {n1}"))
    print()
    for n2 in numeros:
     resultado = n1 * n2   
     print("{:^18}".format(f"{n1} x {n2} = {resultado}"))
    print("#" * 18)



