#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX089: Crie uma programa que leia nome e duas notas
de vários alunos e guarde tudo em uma lista composta. No
final, mostre um boletim contando a média de cada um e
permita que o usúario possa mostrar as notas de cada
aluno individualmente."""

print('\n{:=^30}'.format('Exercicio:089'))

alunos = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1+nota2) / 2
    resp = str(input('Deseja continuar? [S/N]: ')).strip()
    alunos.append([nome, [nota1,nota2], media])

    if resp in 'Nn':
        break
print('-=-'*10)
print(f'{"CODIGO":<4}{"NOME":>8}{"MEDIA":>10}')
print('---'*10)
for pos, b in enumerate(alunos):
    print(f'{pos:<8}{b[0]:<8}{b[2]:>8.1f}')

while True:
    print('-=-'* 10)
    opcao = int(input('Digite o codigo do aluno ou 999 para encerrar: '))
    if opcao == 999:
        print('Programa Finalizado')
        break
    if opcao <= len(alunos) -1:
        print(f'Notas de {alunos[opcao][0]} são {alunos[opcao][1]}')
print('<<<< OBRIGADO >>>>')