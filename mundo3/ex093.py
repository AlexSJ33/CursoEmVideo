#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX093: Crie um programa que gerencie o aproveitamento
de um jogador de futebol. O programa vai ler o nome
do jogador e quantas partidas ele jogou. Depois vai
ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato."""

print('\n{:=^30}'.format('Exercicio:093'))

player = dict()
player['name'] = str(input('Football player name: '))
player['played'] = int(input(f'How many matches did {player["name"]} play? '))
player['goals'] = list()
game = player['played']
for x in range(player['played']):
    player['goals'].append(int(input(f'How many goals in match {x+1}: ')))
player['total'] = sum(player['goals'])

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
