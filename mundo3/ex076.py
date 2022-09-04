#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX076: Crie um programa que tenha uma tupla unica com
nomes de produtos e seus respectivos preços, na sequencia.
No final, mostre uma listagem de preços, organizando os
dados em forma tabular."""

print('\n{:=^30}'.format('Exercicio:076'))
produtos = ('Abacaxi',3.49,
            'Pera',2.40,
            'Limão',0.25,
            'Laranja',1.29,
            'Uva',1.75,
            'Maçã',2)
print('-'*40)
print(f'{"LISTA DE PRODUTO":^40}')
print('-'*40)
for x in range(0,len(produtos)):
    if x % 2 == 0:
        print(f'{produtos[x]:.<30}',end='')
    else:
        print(f'R${produtos[x]:>7.2f}')
print('-'*40)
