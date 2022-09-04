#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX071: Crie um programa que simule o funcionamento
de um caixa eletrônico. No início, pergunte ao usuário
qual será o valor a ser sacado (número inteiro) e o
programa vai informar quantas cédulas de cada valor
serão entregues.
OBS:
Considere que o caixa possui cédulas de R$50,R$20,R$10 e R$1 ."""

print('\n{:=^30}'.format('Exercicio:071'))

print('-'*30)
print('{:^30}'.format('CAIXA ELETRONICO 24hs'))
print('-'*30)
valor = int(input('Informe o valor para saque: R$ '))
print('-'*30)

total = valor
cedula = 50
cont_cedula = 0
while True:
    if total >= cedula:
        total -= cedula
        cont_cedula +=1
    else:
        if cont_cedula > 0:
            print(f'Total de {cont_cedula} cédula(s) de R$ {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 1
        cont_cedula = 0
        if total == 0:
            break
