#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX039: Faça um programa que leia o ano de nascimento
de um jovem e informe, de acordo com sua idade:
-Se ele ainda vai se alistar ao serviço militar.
-Se é a hora de se alistar.
-Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que faltou ou que passou do prazo. """

from datetime import date
print('\n{:=^30}'.format('Exercicio:039'))
nasc = int(input('Informe o ano de nascimento:'))
atual = date.today().year
idade = atual - nasc
if idade < 18:
    print('Faltam {} anos para você se alistar ao serviço militar.'.format(18-idade))
elif idade == 18:
    print('Você tem {} anos\nJá está na hora do seu alistamento ao seviço militar.'.format(idade))
else:
    print('Idade: {} anos\nSeu alistamento militar já passou.'.format(idade))
    print('Seu prazo foi a {} anos atras'.format(idade-18))
