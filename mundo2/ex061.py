#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX061: Refaça o DESAFIO 051, lendo o primeiro
termo e a razão de uma PA, mostrando os 10
primeiros termos da progressão usando a estrutura while."""

print('\n{:=^30}'.format('Exercicio:061'))

t = int(input('Digite o primeiro termo:'))
r = int(input('Digite a razão:'))
f = 1
while f <= 10:
    t = t+r
    f += 1
    print(t-r,end='-->')
print('FIM')

"""
for x in range(10):
    t = t+r
    print(t-r,end='-->')
print('FIM')"""
    