#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX028: Escreva um programa que faça o computador
"pensar" em um numero inteiro entre 0 e 5
e peça para o usuario tentar descobrir qual foi
o numero escolhido pelo computador
O programa deverá escrever na tela
se o usuario venceu ou perdeu. """

print('\n{:=^30}'.format('Exercicio:028'))
from random import randint
num = randint(0,5)
n = int(input('Qual numero eu pensei? '))
if n == num:
    print('Você Venceu ! Numero escolhido {}'.format(num))
else:
    print('Você Perdeu ! Numero escolhido {}'.format(num))