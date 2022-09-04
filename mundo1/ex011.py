#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX011: Faça um programa que leia a largura e altura de uma parede
        em metros, calcule sua área e a quantidade de tinta necessária
        para pinta-la sabendo que cada litro de tinta pinta uma área de 2m²."""

print('\n{:=^30}'.format('Exercicio:011'))
largura = float(input('Informe a Largura da Parade em metros: '))
altura = float(input('Informe a Altura da Parade em metros: '))
area = largura*altura
tinta = area / 2
print('Tamanho da parade = {}m²\nQuantidade necessária: {:.1f}L de tinta'.format(area,tinta))