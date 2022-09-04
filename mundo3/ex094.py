#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX094: Crie um programa que leia nome, sexo e
idade de várias pessoas, guardando os dados de cada
pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade do grupo
C) Uma lista com todas as mulheress.
D) Uma lista com todas as pessoas com idade acima da média"""

print('\n{:=^30}'.format('Exercicio:094'))

g = list()
p = dict()
soma = media = 0
while True:
    p.clear()
    p['name'] = str(input('Name: '))
    p['gender'] = str(input('Gender:[M/F] '))
    while p['gender'] not in 'MmFf':
        p['gender'] = str(input('ERROR! Please just type M or F: '))
    p['age'] = int(input('Age: '))
    soma += p['age']
    g.append(p.copy())
    while True:
        resp = str(input('Do you want to continue? [Y/N]: ').upper()).strip()
        if resp in 'YN':
            break
        print('ERROR! Just answer: [Y/N]')
    if resp == 'N':
        break
print('-=-'*15)
print(f'A) We have {len(g)} people registered in total')
media = soma / len(g)
print(f'B) The average age is {media:3.2f} years old')
print(f'C) The women registered were: ', end='')
for x in g:
    if x['gender'] in 'Ff':
        print(f'{x["name"]} ',end=',')
print()
print(f'D) List of people who are above average')
for p in g:
    if p['age'] >= media:
        print('   ',end='')
        for k, v in p.items():
            print(f'{k} = {v}, ', end='')
        print()
print('<<<<Fim do Programa>>>>')
