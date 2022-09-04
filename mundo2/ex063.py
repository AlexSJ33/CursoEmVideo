#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX063: Escreva um programa que leia um numero N
inteiro qualquer e mostre na tela os N primeiros
elementos de uma Sequencia Fibonacci.
Exemplo: 0, 1, 1, 2, 3, 5, 8"""

print('\n{:=^30}'.format('Exercicio:063'))
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('{}->{}'.format(t1,t2),end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print('->{}'.format(t3),end='')
    t1 = t2
    t2 = t3
    cont +=1
print('-> FIM')