#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX054: Crie um programa que leia o ano de nascimento
de sete pessoas. No final, mostre quantas pessoas
ainda não atingiram a maioridade e quantas já são maiores."""

print('\n{:=^30}'.format('Exercicio:054'))
from datetime import date
maior = 0
menor = 0
atual = date.today().year
for x in range(1,8):
    ano = int(input('Digite o ano de Nascimento da {}ª Pessoa: '.format(x)))
    if (atual - ano) >= 18:
        maior = maior + 1
    else:
        menor = menor + 1
print('{} Pessoas menores de idade\n{} Pessoas maiores de idade'.format(menor,maior))
