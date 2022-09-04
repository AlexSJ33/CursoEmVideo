#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX062: Melhore o DESAFIO 061, perguntando para
o usuario se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer
mostrar 0 termos."""

print('\n{:=^30}'.format('Exercicio:062'))
t = int(input('Digite o primeiro termo:'))
r = int(input('Digite a razão:'))
cont = 1
total = 0
mais = 10
while mais != 0: 
    total = total + mais
    while cont <= total:
        t = t+r
        cont += 1
        print(t-r,end='-->')
    print('PAUSA..')
    mais = int(input('Quantos termo você quer mostrar a mais? '))


print('Progressão finalizada. Foram mostrados {} termos'.format(total))