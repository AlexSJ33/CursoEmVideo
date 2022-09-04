#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX024: Crie uma programa que leia o nome
de uma cidade e diga se ela começa ou não
com o nome: 'Santo'. """

print('\n{:=^30}'.format('Exercicio:024'))
cidade = str(input('Digite a cidade: ')).strip()
print(cidade[:5].upper() == 'SANTO')
