#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX014: Escreva um programa que converta uma temperatura
        digitando em graus Celsius e converta para graus Fahrenheit."""

print('\n{:=^30}'.format('Exercicio:014'))
c = float(input('Informe a temperadura em graus Celsius: '))
f = ((9*c)/5)+32
print('A temperatura de {} graus C corresponde a {} graus F'.format(c,f))