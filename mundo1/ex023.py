#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX023: Faça um programa que leia um numero de 0 a 9999
e mostre na tela cada um dos digitos separados.
Exemplo: Digite um numero: 1834
unidade:4
dezena:3
centena:8
milhar:1 """

print('\n{:=^30}'.format('Exercicio:023'))
num = int(input('Didigite um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('unidade:{}\ndezena:{}\ncentena:{}\nmilhar:{}'.format(u,d,c,m))