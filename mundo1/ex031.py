#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX031: Desenvolva um programa que pergunte a 
distancia de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0.50 por km
para viagens de até 200km e R$0.45 para viagens mais longas. """

print('\n{:=^30}'.format('Exercicio:031'))
d = float(input('Informe a distancia da viagem: '))
if d <= 200:
    valor = (d * 0.50)
else:
    valor = (d * 0.45)
print('Distancia = {}Km\nValor da Passagem: R$ {:.2f}'.format(d,valor))