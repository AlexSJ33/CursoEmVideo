#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX079: Crie um programa onde o usuario possa
digitar varios valores numericos e cadastre-os 
em uma lista. Caso o número ja exista la dentro,
ele não será adicionado.
No final, serão exibidos todos os valores únicos
digitados, em ordem crescente."""

print('\n{:=^30}'.format('Exercicio:079'))

lst = []

while True:
    num = int(input('Digite um valor: '))
    if num in lst:
        print('Esse número já foi cadastrado. Tente outro !')
    else:
        lst.append(num)
        res = str(input('Deseja continuar? [S/N]'))
        lst.sort()
    if res in 'Nn':
        break    
print(f'Valores digitados foram: ',end='')
for x in lst:
    print(f'{x} ',end='')
print()