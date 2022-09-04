#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX042: Refaça o DESAFIO 035 dos triângulos, acrescentando
o recurso de mostrar que tipo de triângulo será formado:
-Equilátero: todos os lados são iguais
-Isósceles: dois lados iguais
-Escaleno: todos os lados diferentes"""

print('\n{:=^30}'.format('Exercicio:042'))
r1 = float(input('Informe o comprimento da primeira reta: '))
r2 = float(input('Informe o comprimento da segunda reta: '))
r3 = float(input('Informe o comprimento da terceira reta: '))
if r1 == r2 == r3:
    print('-Equilátero: todos os lados são iguais')
elif r1 == r2 or r2 == r3 or r1 == r3:
    print('-Isósceles: dois lados iguais')
else:
    print('-Escaleno: todos os lados diferentes')