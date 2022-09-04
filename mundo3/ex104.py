#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX104: Crie um programa que tenha a função leiaInt(), que
vai funcionar de forma semelhante à função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n')"""
#Exemplo:
# ------------------------------------------------
# Programa principal
# n = leiaInt('Digite um número: ')
# print(f'Você acabou de digitar o número {n}')
# ------------------------------------------------
# Digite um número: w
# ERRO! Digite um número inteiro válido
# ------------------------------------------------
print('\n{:=^30}'.format('Exercicio:104'))

def leiaInt(num):
    resp = False
    valor = 0
    while True:
        n = str(input(num))
        if n.isnumeric():
            valor = int(n)
            resp = True
        else:
            print('\033[0;33mERRO! Digite um número válido.\033[m')
        if resp:
            break
    return valor
        
#PROGRAMA PRINCIPAL
n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')