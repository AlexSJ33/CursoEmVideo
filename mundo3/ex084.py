#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX084: Faça um programa que leia nome e peso de varias pessoas,
guardando tudo em uma lista. No final mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""

print('\n{:=^30}'.format('Exercicio:084'))


dados = []
pessoas = []
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
        
    pessoas.append(dados[:])
    dados.clear()

    resp = str(input('Quer continuar? [S/N]: ')).strip()
    
    if resp in 'Nn':
        break


print(f'Foram cadastradas {len(pessoas)} Pessoas')
print(f'O maior peso foi {maior}Kg. ',end='')
for x in pessoas:
    if x[1] == maior:
        print(f'{x[0]}',end='')
print()    
print(f'O menor peso foi {menor}Kg. ',end=' ')
for x in pessoas:
    if x[1] == menor:
        print(f'{x[0]}', end=' ')
print()