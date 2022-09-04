#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX078: Faça um programa que leia 5 valores numéricos
e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado
e as suas respectivas posições na lista. """

print('\n{:=^30}'.format('Exercicio:078'))
valores = []
maior = menor = 0
for cont in range(0,5):
    valores.append(int(input(f'Digite um valor na posição {cont}: ')))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]
print(f'O Maior numero foi {maior}, nas posições: ', end='')
for pos, v in enumerate(valores):
    if v == maior:
        print(f'{pos}...',end='')
print()
print(f'O Menor numero foi {menor}, nas posições: ' ,end='')
for pos, v in enumerate(valores):
    if v == menor:
        print(f'{pos}...',end='')
print()

