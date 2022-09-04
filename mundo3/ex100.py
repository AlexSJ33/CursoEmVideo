#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX100: Faça um programa que tenha uma lista chamada numeros
e duas funçoes chamadas sorteia() e somaPar(). A primeira função
vai sortear 5 numeros e vai coloca-los dentro da lista e a segunda
função vai mostrar a soma entre todos os valores PARES
sorteados pela função anterior."""

#Exemplo:
# Sorteando 5 valores da lista: 9 8 2 2 3 PRONTO!
# Somando os valores PARES de [9 8 2 2 3], temos12

from time import sleep
from random import randint

numeros = []

def sorteia():
    print('Sorteando 5 numeros: ',end='')

    for x in range(5):
        num =  randint(0,10)
        numeros.append(num)
        x +=1
        print(num,end='.. ',flush=True)
        sleep(0.8)
    print('PRONTO!')
    
def somaPar():
    cont = 0
    for x in numeros:
        if x % 2 == 0:
            cont += x
    print(f'Somando os valores PARES de {numeros}, temos: {cont}')

sorteia()
somaPar()
