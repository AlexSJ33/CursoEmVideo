#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX077: Crie um programa que tenha uma tupla com várias
palavras (não usar acentos). Depois disso, você deve mostrar
para cada palavra, quais são as suas vogais. """

print('\n{:=^30}'.format('Exercicio:077'))
print('-'*30)
print(f'{"VAMOS APRENDER VOGAIS":^30}')
print('-'*30)
palavras = ('carro','abacaxi','tesoura','bicicleta',
            'automovel','caderno','placar','roleta')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
print()
print('-'*30)

