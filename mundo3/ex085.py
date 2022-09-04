#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX085: Crie um programa onde o usuario possa digitar
sete valores numericos e cadastre-os em uma lista única
que mantenha separados os valores pares e impares. No final,
mostre os valores pares e impares em ordem crescente"""

print('\n{:=^30}'.format('Exercicio:085'))


valores = [[],[]]
for x in range(0,7):
    num = int(input(f'Digite o {x+1}º valor: '))
    if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1].append(num)
valores[0].sort()
valores[1].sort()
print(f'Os valores pares foram: {valores[0]}')
print(f'Os valores ímpares foram: {valores[1]}')