#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX009: Escreva um programa que leia um numero inteiro qualquer
         e mostre na tela a sua tabuada"""

print('\n{:=^30}'.format('Exercicio:009'))
num = int(input('Digite um numero para ver sua tabuada: '))
for x in range(0,11):
    print('{} x {} = {}'.format(num, x, num*x))