#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX050: Desenvolva um programa que leia seis
numeros inteiros e mostre a soma apenas daqueles
que forem pares. Se o valor digitado for impar, desconsidere-o"""

print('\n{:=^30}'.format('Exercicio:050'))
contador = 0
for x in range(6):
    n = int(input('Insira seis numeros: '))
    if n % 2 == 0:
        contador +=n
print('A soma entre os numeros é {}'.format(contador))

