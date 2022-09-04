#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX046: Faça um programa que mostre na tela uma contagem
regressiva para o estouro de fogos de artifício, indo de
10 até 0, com uma pausa de 1 segundo entre eles."""

print('\n{:=^30}'.format('Exercicio:046'))
from time import sleep
msg = 'Feliz Ano Novo !!'
for x in range(10, -1, -1):
    sleep(1)
    print(x)
for i in msg:
    print(i, end='', flush=True)
    sleep(.10)
print()