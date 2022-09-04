#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX032: Faça um programa que leia um ano qualquer
e mostre se ele é BISSEXTO. """

print('\n{:=^30}'.format('Exercicio:032'))
from datetime import date
ano = int(input('Informe um ano qualquer, ou digite "0" para o ano atual: ').strip())
if ano == 0:
    ano = date.today().year
if (ano % 4 == 0):
    if (ano % 100 == 0):
        if (ano % 400 == 0):
            print('{} É Ano Bissexto'.format(ano))
        else:
            print('{} NÃO é Ano Bissexto'.format(ano))
    else:
        print('{} É Ano Bissexto'.format(ano))
else:
    print('{} NÃO é Ano Bissexto'.format(ano))
