#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX060: Faça um programa que leia um numero
qualquer e mostre seu fatorial.
Exemplo: 5! = 5x4x3x2x1=120"""

print('\n{:=^30}'.format('Exercicio:060'))
n = int(input('Digite um numero: '))
c = n
f = 1
print('Calculando Fatorial {}!'.format(n))
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))