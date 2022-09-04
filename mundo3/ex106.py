#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX106: Faça um mini-sistema que utilize o Interactive Help
do Python. O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
OBS: use cores."""
#Exemplo:
# ---------------------------
# SISTEMA DE AJUDA PyHELP
# ---------------------------
# Função ou Biblioteca > len
# -----------------------------------
# Acessando o manual do comando 'len'
# -----------------------------------
#Help on built-in function len in module builtins:
#len(obj, /)
#   Return the number of items in a container.
# ---------------------------
# SISTEMA DE AJUDA PyHELP
# ---------------------------
# Função ou Biblioteca > fim
# ----------
# ATÉ LOGO!
# ----------
print('\n{:=^30}'.format('Exercicio:106'))
from time import sleep

def manual(man):
    cabecalho(f'Acessando o manual do comando \'{man}\'', 4)
    print(cores[6],end='')
    sleep(2)
    help(man)
    print(cores[0],end='')
    sleep(2)
    
def cabecalho(msg,cor=0):
    tamanho = len(msg) + 5
    print(cores[cor],end='')
    print('-' * tamanho)
    print(f'  {msg}')
    print('-' * tamanho)
    print(cores[0],end='')
    

#PROGRAMA PRINCIPAL
cores = ('\033[m',         # 0 - sem cores
         '\033[0;33;41m',  # 1 - vermelho
         '\033[0;30;42m',  # 2 - verde
         '\033[0;30;43m',  # 3 - amarelo
         '\033[44m',  # 4 - azul
         '\033[0;30;45m',  # 5 - roxo
         '\033[7;30m'      # 6 - branco
         )
m = ''
while True:
    cabecalho('SISTEMA DE AJUDA PyHELP', 2)
    m = str(input('Função ou Biblioteca > '))
    if 'fim' in m.strip().lower():
        break
    else:
        manual(m)
cabecalho('ATÉ LOGO!', 1)
