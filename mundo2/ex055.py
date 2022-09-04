#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX055: Faça um programa que leia o peso de 
cinco pessoas. No final mostre qual foi o maior
e o menor peso lidos."""

print('\n{:=^30}'.format('Exercicio:055'))
maior = 0
menor = 0
for pessoa in range(1,6):
    peso = float(input('Digite o peso da {}ª Pessoa: '.format(pessoa)))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso


print('Maior Peso: {}Kg\nMenor Peso: {}Kg'.format(maior,menor))
