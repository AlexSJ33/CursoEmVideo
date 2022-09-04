#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX051: Desenvolva um programa que leia o primeiro
termo e a razão de uma PA. No final, mostre os 10
primeiros termos dessa progressão."""

print('\n{:=^30}'.format('Exercicio:051'))
t = int(input('Digite o primeiro termo:'))
r = int(input('Digite a razão:'))

for x in range(10):
    t = t+r
    print(t-r,end='-->')
print('FIM')
    