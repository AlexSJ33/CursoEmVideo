#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX074: Crie um programa que vai gerar cinco numeros aleatorios
e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique
o menor e o maior valor que estão na tupla."""

print('\n{:=^30}'.format('Exercicio:074'))
from random import randint
n=((randint(1,10)),(randint(1,10)),(randint(1,10)),(randint(1,10)),(randint(1,10)))
for x in n:
    print(x,end=' ')
print(f'\nO menor numero encontrado foi {min(n)}')
print(f'\nO maior numero encontrado foi {max(n)}')
print(type(n))
