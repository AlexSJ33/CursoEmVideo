#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX067: Faça um programa que mostre a tabuada de
vários números, um de cada vez, para cada valor
digitado pelo usuário. O programa será interrompido
quando o número solicitado for negativo."""

print('\n{:=^30}'.format('Exercicio:067'))
print('{:^30}'.format('TABUADA'))


while True:
    print('~'*30)
    n = int(input('Digite um número: '))
    print('~'*30)
    if n < 0:
        break
    else:
        for x in range(1,11):
            print(f'{n} x {x} = {x*n}')
