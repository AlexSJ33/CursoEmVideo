#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX047: Crie um programa que mostre na tela todos
os numeros pares que estão no intervalo entre 1 e 50."""

print('\n{:=^30}'.format('Exercicio:047'))
for x in range(1, 50+1):
    if x % 2 == 0:
        print(x, end=',')