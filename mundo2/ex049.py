#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX049: Refaça o DESAFIO 009, mostrando a tabuada
de um numero que o usuario escolher, só que
agora utilizando um laço for."""

print('\n{:=^30}'.format('Exercicio:049'))

num = int(input('Digite um numero para ver sua tabuada: '))
for x in range(0,11):
    print('{} x {} = {}'.format(num, x, num*x))