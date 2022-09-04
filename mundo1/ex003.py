#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''EX003: Crie um programa que leia dois números e mostre a soma entre eles.'''

print('\n{:=^30}'.format('Exercicio:003'))
n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro número: '))

soma = n1 + n2
print('A soma entre {} e {} é igual: {}'.format(n1,n2,soma))
