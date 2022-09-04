#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX070: Crie um programa que leia o nome e o preço
de vários produtos. O programa deverá perguntar se o
usuário vai continuar.
No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000,00.
C) Qual é o nome do produto mais barato."""

print('\n{:=^30}'.format('Exercicio:070'))
from time import sleep
cont = menor = mil = total = 0
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$ '))
    total +=preço
    cont +=1
    if preço > 1000.00:
        mil +=1
    if cont == 1:
        menor = preço
        nome = produto
    else:
        if preço < menor:
            menor = preço
            nome = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Continuar comprando?[S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('-'*30)
print('Finalizando, aguarde...')
print('-'*30)
sleep(3)
print(f'O total da sua compra foi R$ {total:.2f}')
print(f'Foram encontrados {mil} produtos que custam mais de R$1000,00')
print(f'O produto mais barato foi {nome}, que custa R$ {menor:.2f}')
