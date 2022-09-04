#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX016: Crie um programa que leia um número Real qualquer
pelo teclado e mostre na tela sua proção Inteira.
EX:
Digite um número: 6.127
O número 6.127 tem a parte Inteira 6. """

from math import trunc
print('\n{:=^30}'.format('Exercicio:016'))
real = float(input('Digite um número com casas decimais: '))
print('O número {} tem a parte Inteira {}'.format(real, trunc(real)))