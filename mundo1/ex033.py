#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX033: Faça um programa que leia três numeros
e mostre qual é o maior e qual é o menor. """

print('\n{:=^30}'.format('Exercicio:033'))
n1 = float(input('Primeiro numero: ').strip())
n2 = float(input('Segundo numero: ').strip())
n3 = float(input('Terceiro numero: ').strip())
if (n1 > n2) and (n1 > n3):
    maior = n1
    if n2 < n3:
        menor = n2
    else:
        menor = n3
elif (n2 > n1) and (n2 > n3):
    maior = n2
    if n1 < n3:
        menor = n1
    else:
        menor = n3
else:
    maior = n3
    if n1 < n2:
        menor = n1
    else:
        menor = n2

print('O maior numero foi {}\nO menor numero foi {}'.format(maior,menor))