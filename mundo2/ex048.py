#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX048: Faça um programa que calcule a soma entre
todos os numeros impares que são multiplos de tres
e que se encontram no intervalo de 1 até 500."""

print('\n{:=^30}'.format('Exercicio:048'))

soma = 0
contador = 0
for x in range(1, 501, 2):
    if x % 3 == 0:
        contador += 1
        soma +=x

print('A soma de todos os {} valores solicitados é {}'.format(contador,soma))