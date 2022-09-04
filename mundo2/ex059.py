#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX059: Crie um programa que leia dois valores
e mostre um menu na tela:
[1]somar
[2]multiplicar
[3]maior
[4]novos numeros
[5]sair do programa
Seu programa deverá realizar a operação
solicitada em cada caso."""

print('\n{:=^30}'.format('Exercicio:059'))
n1 = float(input('Insira o primeiro numero: '))
n2 = float(input('Insira o segundo numero: '))

print('')
opt = 0

while opt != 5:
    print('-='*12)
    print('[1] - Somar\n[2] - Multiplicar\n[3] - Maior\n[4] - Novos Numeros\n[5] - Sair do programa')
    print('-='*12)
    opt = int(input('Escolha uma opção: '))
    if opt == 1:
        print('\nA soma de {} + {} = {}'.format(n1,n2, n1+n2))
    if opt == 2:
        print('\nMultiplicando {} x {} = {}'.format(n1,n2, n1*n2))
    if opt == 3:
        maior = 0
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('\nMaior número: {}'.format(maior))
    if opt == 4:
        n1 = float(input('Insira o primeiro numero: '))
        n2 = float(input('Insira o segundo numero: '))
    if opt > 5:
        print('Opção invalida. Tente novamente!')
print('Programa encerrado...')
