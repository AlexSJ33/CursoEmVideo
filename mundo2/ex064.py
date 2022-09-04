#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX064: Crie um programa que leia varios
numeros inteiros pelo teclado. O programa só
vai parar quando o usuario digitar o valor
999, que é a condição de parada. No final,
mostre quantos numeros foram digitados e
qual foi a soma entre eles (desconsiderando o flag)"""

print('\n{:=^30}'.format('Exercicio:064'))

c = 0
soma = 0
while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    else:
        c += 1
        soma +=n

#print('Voce digitou {} numero(s) e a soma é = {}'.format(c,soma))
print(f'Voce digitou {c} numero(s) e a soma é = {soma}')