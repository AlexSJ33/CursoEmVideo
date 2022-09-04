#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX045: Crie um programa que faça o computador jogar
Jokenpô com você."""

print('\n{:=^30}'.format('Exercicio:045'))
import sys
from time import sleep
from random import randint

print('Bem vindo ao Game JOKENPÔ.')
print('Para jogar basta digitar o numero correspondente a sua opção!')
print('1 - Pedra\n2 - Papel\n3 - Tesoura')

melhor3x = str(input('Melhor de Três? S/N: ').upper())

tentativas = 0
placar_jogador = 0
placar_cpu = 0
if melhor3x == 'S':
    tentativas = 3
elif melhor3x == 'N':
    tentativas = 1
else:
    print('\nOpção inválida...\nPrograma encerrado!')
    sys.exit()

for x in range(tentativas):
    try:            
        jogador = int(input('Faça sua escolha:'))
        if jogador != 1 and jogador != 2 and jogador != 3:
            print('\nOpção inválida...\nPrograma encerrado!')
            sys.exit()
        else:
            tentativas =-1
            cpu = randint(1,3)
    except ValueError:
        print('\nOpção inválida...\nPrograma encerrado!')
        sys.exit()

    if jogador == 1 and cpu == 1:
        print('JOOO..')
        sleep(2)
        print('KEEN..')
        sleep(2)
        print('POOO !!..\n')
        sleep(1)
        print('JOGADOR : Pedra !')
        print('CPU: Pedra')
        print('Empate')
    elif jogador == 1 and cpu == 2:
        print('JOOO..')
        sleep(2)
        print('KEEN..')
        sleep(2)
        print('POOO !!..\n')
        sleep(1)
        print('JOGADOR : Pedra !')
        print('CPU: Papel')
        print('Vitoria: CPU')
        placar_cpu = placar_cpu + 1
    elif jogador == 1 and cpu == 3:
        print('JOOO..')
        sleep(2)
        print('KEEN..')
        sleep(2)
        print('POOO !!..\n')
        sleep(1)
        print('JOGADOR : Pedra !')
        print('CPU: Tesoura')
        print('Vitoria: Jogador')
        placar_jogador =placar_jogador + 1

    elif jogador == 2 and cpu == 1:
        print('JOOO..')
        sleep(2)
        print('KEEN..')
        sleep(2)
        print('POOO !!..\n')
        sleep(1)
        print('JOGADOR : Papel !')
        print('CPU: Pedra')
        print('Vitoria: Jogador')
        placar_jogador =placar_jogador + 1
    
    elif jogador == 2 and cpu == 2:
        print('JOOO..')
        sleep(2)
        print('KEEN..')
        sleep(2)
        print('POOO !!..\n')
        sleep(1)
        print('JOGADOR : Papel !')
        print('CPU: Papel')
        print('Empate')
    
    elif jogador == 2 and cpu == 3:
        print('JOOO..')
        sleep(2)
        print('KEEN..')
        sleep(2)
        print('POOO !!..\n')
        sleep(1)
        print('JOGADOR : Papel !')
        print('CPU: Tesoura')
        print('Vitoria: CPU')
        placar_cpu = placar_cpu + 1

    elif jogador == 3 and cpu == 1:
        print('JOOO..')
        sleep(2)
        print('KEEN..')
        sleep(2)
        print('POOO !!..\n')
        sleep(1)
        print('JOGADOR : Tesoura !')
        print('CPU: Pedra')
        print('Vitoria: CPU')
        placar_cpu = placar_cpu + 1

    elif jogador == 3 and cpu == 2:
        print('JOOO..')
        sleep(2)
        print('KEEN..')
        sleep(2)
        print('POOO !!..\n')
        sleep(1)
        print('JOGADOR : Tesoura !')
        print('CPU: Papel')
        print('Vitoria: Jogador')
        placar_jogador =placar_jogador + 1

    elif jogador == 3 and cpu == 3:
        print('JOOO..')
        sleep(2)
        print('KEEN..')
        sleep(2)
        print('POOO !!..\n')
        sleep(1)
        print('JOGADOR : Tesoura !')
        print('CPU: Tesoura')
        print('Empate')
    else:
        print('\nOpção inválida...\nPrograma encerrado!')
        sys.exit()

print('>>>>PLACAR<<<<')
print('Jogador: {} x {} CPU'.format(placar_jogador,placar_cpu))
