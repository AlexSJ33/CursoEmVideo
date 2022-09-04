#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX091: Crie um programa onde 4 jogadores joguem
um dado e tenham resultados aleatórios. Guarde esses
resultados em um dicionário em Python. No final, coloque
esse dicionário em ordem, sabendo que o vencedor tirou o
maior número no dado."""

print('\n{:=^30}'.format('Exercicio:091'))

from random import randint
from time import sleep
from operator import itemgetter

game = {'player_1': randint(1,6),
        'player_2': randint(1,6),
        'player_3': randint(1,6),
        'player_4': randint(1,6)}
ranking = list()
print('{:^30}'.format('DRAWN VALUES'))
for k, v in game.items():
    print(f'{k}  The number drawn was... {v}.')
    sleep(1)
ranking = sorted(game.items(), key= itemgetter(1), reverse=True)
print('-=-'*12)
print('{:^30}'.format('RANKING OF PLAYER'))
for i, v in enumerate(ranking):
    print(f'{i+1}º place: {v[0]} with {v[1]}')
    sleep(1)
