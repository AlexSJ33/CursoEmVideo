#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''EX008: Escreva um programa que leia um valor em metros
 e o exiba convertido em centímetros e milímetros.'''

print('\n{:=^30}'.format('Exercicio:008'))
num = float(input('Digite uma distancia em metros: '))
km = num / 1000
cm = num * 100
dm = num * 10
mm = num * 1000
hm = num / 100
dam = num / 10

print('A medida de {}m corresponde a\n{}km >>> Kilômetros\n{}hm >>> Hectômetros\n{}dam >>> Decâmetros\n{}dm >>> Decímetros\n{}cm >>> Centímetros\n{}mm >>> Milímetros'.format(num, km, hm, dam, dm, cm, mm))

