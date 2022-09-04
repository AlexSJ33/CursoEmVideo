#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX030: Crie um program que leia um numero inteiro
e mostre na tela se ele é par ou impar """

print('\n{:=^30}'.format('Exercicio:030'))
n = int(input('Insira um numero:'))
if (n % 2 == 0):
    print('{} é Par'.format(n))
else:
    print('{} é Impar'.format(n))