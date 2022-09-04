#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX090: Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário. No final, mostre
o conteúdo da estrutura na tela."""

print('\n{:=^30}'.format('Exercicio:090'))

aluno = dict()
aluno['nome'] = str(input('Nome do Aluno: '))
aluno['media'] = float(input('Média do Aluno: '))
print('-=-'*10)
if aluno['media'] <= 5:
    aluno['situação'] = 'REPROVADO'
elif aluno['media'] > 5 and aluno['media'] <= 7:
    aluno['situação'] = 'RECUPERAÇÃO'
else:
    aluno['situação'] = 'APROVADO'
    
print(f'ALUNO: {aluno["nome"]} \nMÉDIA: {aluno["media"]} \nSITUAÇÃO: {aluno["situação"]}')

