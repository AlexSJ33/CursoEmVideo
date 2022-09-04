#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX088: Faça um programa que ajude um jogador da MEGA SENA
a criar palpites. O programa vai perguntar quantos jogos serão
gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta."""

print('\n{:=^30}'.format('Exercicio:088'))

from random import randint
from time import sleep
lista_num = []

qtde = 0
jogos = []
print('-='*15)
print('    MEGA SENA ACUMULADA    ')
print('-='*15)
num_jogos = int(input('Quantos jogos gostaria de fazer? '))
print('--'*15)

while qtde < num_jogos:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista_num:
            lista_num.append(num)
            cont += 1
        if cont >= 6:
            break
    lista_num.sort()
    jogos.append(lista_num[:])
    lista_num.clear()
    qtde += 1
print('-=-'* 2, f'SORTENDO {qtde} JOGOS','-=-'* 2)
for pos, j in enumerate(jogos):
    print(f'Jogo {pos+1}: {j}')
    sleep(1)
print('-=-'* 3, f'BOA SORTE','-=-'* 3)
