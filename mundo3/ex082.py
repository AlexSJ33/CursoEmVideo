#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX082: Crie um programa que vai ler varios numeros
e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter
apenas os valores pares e os valores impares digitados
respectivamente.
Ao final mostre o conteudo das tres listas geradas."""

print('\n{:=^30}'.format('Exercicio:082'))

pares = []
impares = []
valores = []

while True:
    valores.append(int(input('Digite o valor: ')))
    res = str(input('Deseja continuar? [S/N]'))
    if res in 'Nn':
        break
for x in valores:
    if x % 2 == 0:
        pares.append(x)
    else:
        impares.append(x)
print(f'Sua lista: {valores}')
print(f'Lista com pares: {pares}')
print(f'Lista com impares: {impares}')