#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX096: Faça um programa que tenha uma função chamada area(),
que receba as dimensões de um terreno retangular (largura e comprimento)
e mostre area do terreno."""

# Exemplo:
# Controle de Terrenos
#---------------------
#LARGURA (m): 4.5
#COMPRIMENTO (m): 8
#A Area de um terreno 4.5x8.0 é 36.0m2.

print('\n{:=^30}'.format('Exercicio:096'))
print()
def mostrarLinha(msg):
    print(msg)
    print('-'* len(msg))

def area(larg, comp):
    area = larg * comp
    print(f'A Area de um terreno {larg}x{comp} é {area}m2.')
    print()

mostrarLinha('Controle de Terrenos')
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))

area(l,c)