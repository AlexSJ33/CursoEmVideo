#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX065: Crie um programa que leia varios numeros
inteiros pelo teclado. No final da execução, mostre
a média entre todos os valores e qual foi o maior
e o menor valores lidos. O programa deve perguntar 
ao usuario se ele quer ou não continuar a digitar valores."""

print('\n{:=^30}'.format('Exercicio:065'))

cont = 0
soma = 0
menor = 0
maior = 0
stop = False
while stop == False:
    num = int(input('Digite um número: '))
    resp = str(input('Quer Continuar? [S/N]').upper()[0])
    if resp == 'N':
        stop = True
    cont +=1
    soma += num
    media = soma / cont

    if cont == 1:    
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num


print('Você digitou {} numero(s)'.format(cont))
print('A média entre todos os numeros é {}'.format(media))   
print('O maior valor é {}'.format(maior))
print('O menor valor é {}'.format(menor))
