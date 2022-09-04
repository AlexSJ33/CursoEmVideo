#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX053: Crie um programa que leia uma frase
qualquer e diga se ela é um palindromo, desconsiderando
os espaços. Ex: APOS A SOPA"""

print('\n{:=^30}'.format('Exercicio:053'))
frase = str(input('Digite algo: ').strip())
separado = frase.split()
junto = ''.join(separado)

if junto[::-1] == junto:
    print('É um palindromo')
else:
    print('Não é palindromo')
print(junto)
print(junto[::-1])
