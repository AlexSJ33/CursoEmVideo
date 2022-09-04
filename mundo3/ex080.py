#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX080: Crie um programa onde o usuario possa
digitar cinco valores numericos e cadastre-os em
uma lista, já na posição correta de inserção
(sem usar o sort()).
No final, mostre a lista ordenada na tela."""

print('\n{:=^30}'.format('Exercicio:080'))

lst = []
for v in range(0,5):
    num = int(input('Digite um numero: '))
    if v == 0 or num > lst[-1]:
        lst.append(num)
        print('Adicionado ao final da Lista')
    else:
        posição = 0
        while posição < len(lst):
            if num <= lst[posição]:
                lst.insert(posição,num)
                print(f'Adicionado na posição {posição} da lista...')
                break
            posição +=1
print(f'Valor em Ordem: {lst}')
