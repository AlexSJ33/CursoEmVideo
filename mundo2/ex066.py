#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX066: Crie um programa que leia vários números inteiros
pelo teclado. O programa só vai parar quando o usuário digitar
o valor 999, que é a condição de parada. No final, mostre
quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag)."""

print('\n{:=^30}'.format('Exercicio:066'))
c = 0
soma = 0
while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    else:
        c += 1
        soma +=n

print(f'Voce digitou {c} numero(s) e a soma é = {soma}')