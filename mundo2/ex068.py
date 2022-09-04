#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX068: Faça um programa que jogue par ou ímpar
com o computador. O jogo só será interrompido quando o
jogador PERDER, mostrando o total de vitórias consecutivas
que ele conquistou no final do jogo."""

print('\n{:=^30}'.format('Exercicio:068'))
print('{:^30}'.format('JOGO DO PAR OU ÍMPAR'))

from random import  randint
cont = 0
while True:
    
    print('~'*30)
    escolha = str(input('Digite [P]ar ou [I]mpar: ').strip()).upper()[0]
    print('~'*30)
    if 'P' in escolha:
        print('Você escolheu Par')
        num = int(input('Jogue um número: '))
        cpu = randint(0,10)
        soma = num + cpu
        print(f'Computador jogou: {cpu}')
        if soma % 2 == 0:
            print(f'{soma} é PAR. Você venceu !! ')
            cont +=1
        else:
            print(f'{soma} é IMPAR. Você perdeu !!')
            break
        
    if 'I' in escolha:
        print('Você escolheu Ímpar')
        num = int(input('Jogue um número: '))
        cpu = randint(0,10)
        soma = num + cpu
        print(f'Computador jogou: {cpu}')
        if not soma % 2 == 0:
            print(f'{soma} é IMPAR. Você venceu !! ')
            cont +=1
        else:
            print(f'{soma} é PAR. Você perdeu !!')
            break
    else:
        print('Escolha uma opção')
print(f'Vitorias consecutivas {cont}')