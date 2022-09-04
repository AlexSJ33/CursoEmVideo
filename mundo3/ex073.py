#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX073: Crie uma tupla preenchida com os 20 primeiros colocados
da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
Depois mostre:
A) Apenas os 5 primeiros colocados.
B) Os ultimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o Time da Chapecoense."""

print('\n{:=^30}'.format('Exercicio:073'))

"""TABELA
CLASSIFICAÇÃO"""
tabela =('Palmeiras',
'Atlético-MG',
'Fortaleza',
'Bragantino',
'Athletico-PR',
'Flamengo',
'Ceará',
'Bahia',
'Fluminense',
'Santos',
'Atlético-GO',
'Corinthians',
'Internacional',
'Juventude',
'Cuiabá',
'São Paulo',
'Sport',
'América-MG',
'Grêmio',
'Chapecoense')

print('{:-^55}'.format('TABELA CLASSIFICAÇÃO'))
print(tabela)
print('-'*55)
print('Os Cinco Primeiros são: \n')
for pos, nomes in enumerate(tabela[:5]):
    pos+=1
    print(f'{pos} - {nomes}')
print('-'*55)
print('Os Quatro Ultimos são: \n')
for pos, nomes in enumerate(tabela[-4:]):
    pos+=1
    print(f'{pos} - {nomes}')
print('-'*55)
print('Lista em Ordem Alfabética: \n')
print(sorted(tabela))
print('-'*55)
posicao = tabela.index('Chapecoense')
x = posicao+1
print(f'O time da Chapecoense ocupa a {x}ª posição')