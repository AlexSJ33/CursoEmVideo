#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX075: Desenvolva um programa que leia quatro valores pelo
teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os numeros pares"""

print('\n{:=^30}'.format('Exercicio:075'))

num = (int(input('Digite o 1º numero: ')),
       int(input('Digite o 2º numero: ')),
       int(input('Digite o 3º numero: ')),
       int(input('Digite o 4º numero: ')))
print(f'Os números digitados foram {num}')
if not 9 in num:
    print('O valor 9 não apareceu!')
else:
    print(f'O valor 9 apareceu {num.count(9)}x')
if 3 in num:
    print(f'O numero 3 foi digitado na {num.index(3)+1}ª posição')
else:
    print('O numero 3 não foi digitado.')
print('Os valores pares digitados foram: ',end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
print()