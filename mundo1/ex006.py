#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''EX006: Crie um algoritimo que leia um número  e mostre o seu
dobro, triplo e Raiz quadrada.'''

print('\n{:=^30}'.format('Exercicio:006'))
n = int(input('Digite um número: '))

d = n * 2
t = n * 3
r = n ** (1/2)

print('O Dobro de {} vale {}.\nO Triplo de {} vale {}.\nA Raiz quadrada de {} é igual a {:.2f}.'.format(n, d, n, t, n, r))
