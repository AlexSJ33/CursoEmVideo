#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX058: Melhore o jogo do DESAFIO 028 onde
o computador vai 'pensar' em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários
para vencer."""

print('\n{:=^30}'.format('Exercicio:058'))
from random import randint

cpu = randint(0, 10)
tentativa = 1
acertou = False
escolha = int(input('Qual numero estou pensando...? '))
while not acertou:
    if escolha == cpu:
        acertou = True
    if escolha < cpu:
        escolha = int(input('Mais...Tente outra vez: '))
        tentativa +=1
    elif escolha > cpu:
        escolha = int(input('Menos...Tente outra vez: '))
        tentativa +=1
print('Parabéns, você acertou em {} tentativa(s)'.format(tentativa))
