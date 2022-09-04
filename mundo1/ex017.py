#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX017: Faça um programa que leia o comprimento do cateto
 oposto e do cateto adjacente de um triangulo retangulo,
 calcule e mostre o comprimento da hipotenusa """

from math import hypot
print('\n{:=^30}'.format('Exercicio:017'))
b = float(input('Cateto Oposto: '))
a = float(input('Cateto Adjacente: '))
#c = sqrt(pow(b,2) + pow(a,2))
print('O comprimento da hipotenusa é {:.2f}'.format(hypot(b,a)))