#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX069: Crie um programa que leia a idade e o sexo de várias
pessoas. A Cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar.
No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos."""

print('\n{:=^30}'.format('Exercicio:069'))
from time import sleep

cont = homens = mulheres = 0
while True:
    idade = int(input('IDADE: ').strip())
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('SEXO [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        cont += 1
    if sexo == 'M':
        homens += 1

    if sexo == 'F' and idade < 20:
        mulheres += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar?[S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('Gerando relatório, aguarde...\n')
sleep(3)
print(f'Total de pessoas com mais de 18 anos: {cont}')
print(f'Total de homens cadastrados: {homens}')
print(f'Total de mulheres com menos de 20 anos: {mulheres}')