#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX052: Faça um programa que leia um numero inteiro
e diga se ele é ou não um numero primo."""

print('\n{:=^30}'.format('Exercicio:052'))
n = int(input('Digite um numero: '))
contador = 0
for x in range(1,n+1):
    if n % x == 0:
        print('\033[33m', end='')
        contador +=1
    else:
        print('\033[31m', end='')
    print('{} '.format(x),end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(n,contador))
if contador == 2:
    print('{} É número PRIMO !'.format(n))
else:
    print('{} Não é número PRIMO !'.format(n))
