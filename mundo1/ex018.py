#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX018: Faça um programa que leia um angulo qualquer
 e mostre na tela o valor do seno, cosseno e tangente desse angulo """

from math import radians,sin,cos,tan
print('\n{:=^30}'.format('Exercicio:018'))
a = float(input('Informe um angulo qualquer: '))
seno=sin(radians(a))
coss=cos(radians(a))
tange=tan(radians(a))
print('Angulo {}\nSeno = {:.2f}\nCosseno = {:.2f}\nTangente = {:.2f}'.format(a, seno,coss,tange))
