#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX099: Faça um programa que tenha uma função chamada
maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer
qual deles é o maior."""

#Exemplo:
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#Analisando os valores passados...
#4 7 0. Foram informados 3 valores ao todo
#O maior valor informado foi 7.
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#Analisando os valores passados...
#0. Foram informados 1 valores ao todo
#O maior valor informado foi 0.
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

from time import sleep
print('\n{:=^30}'.format('Exercicio:099'))
print()
def maior(*num):
    print('Analisando os valores passados..')
    for x in num:
        print(f'{x}',end=' ', flush=True)
        sleep(0.5)
    print(f'Foram informados {len(num)} valor(es) ao todo')
    print(f'O maior valor informado foi {max(num)}')
    print('-='*15)
    print()

maior(4,7,0)
maior(5,1,81,191,0,3)
maior(6,8,2,6,1)

