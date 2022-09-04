#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX010: Crie um programa que leia quanto dinheiro uma pessoa
         tem na carteira e mostre qauntos Dólares ela pode comprar.
         Considere US$1.00 = R$3,27"""

print('\n{:=^30}'.format('Exercicio:010'))
carteira = float(input('Qual valor em carteira: R$ '))
dolar =carteira / 3.27
print('Você pode comprar com R${:.2f} um valor total de US${:.2f} Dolar(es)'.format(carteira,dolar))