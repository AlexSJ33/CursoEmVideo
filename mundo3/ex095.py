#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX095: Aprimore o DESAFIO 093 para que ele
funcione com vários jogadores, incluindo um
sistema de visualização de detalhes do aproveitamento
de cada jogador."""

print('\n{:=^30}'.format('Exercicio:095'))

time = list()
player = dict()
while True:
    player.clear()
    player['name'] = str(input('Football player name: '))
    player['played'] = int(input(f'How many matches did {player["name"]} play? '))
    player['goals'] = list()
    game = player['played']
    for x in range(player['played']):
        player['goals'].append(int(input(f'How many goals in match {x+1}: ')))
    player['total'] = sum(player['goals'])
    time.append(player.copy())
    resp = str(input('Do you want to continue? [Y/N]').upper()[0])
    if resp == 'N':
        break

print('-=-'*17)
del player['played']

print(player)
print('-=-'*17)
print(f'The name field has the value: {player["name"]}')
print(f'The field goals has the value: {player["goals"]}')
print(f'The total field has the value: {player["total"]}')
print('---'*17)
print(f'The {player["name"]} player, played {game} matches')

for pos, x in enumerate(player["goals"]):
    print(f'>>> In match {pos+1}, he scored {x} goals')

print(f'It was a total of {player["total"]} goals')
