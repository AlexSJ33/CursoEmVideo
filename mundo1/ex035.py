#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX035: Desenvolva um programa que leia
o comprimento de três retas e diga ao usuário
se elas podem ou não formar um triangulo. """

print('\n{:=^30}'.format('Exercicio:035'))
reta1 = float(input('Qual comprimento da primeira reta? '))
reta2 = float(input('Qual comprimento da segunda reta? '))
reta3 = float(input('Qual comprimento da terceira reta? '))
if (reta1 > reta2) and (reta1 > reta3):
    a = reta1
    b = reta2
    c = reta3
elif (reta2 > reta1) and (reta2 > reta3):
    a = reta2
    b = reta1
    c = reta3
else:
    a = reta3
    b = reta1
    c = reta2
if (a< b+c):
    print('As retas {},{},{} podem SIM, formar um triangulo'.format(reta1,reta2,reta3))
else:
    print('Essas medidas não formam um triangulo')

