#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha."""

print('\n{:=^30}'.format('Exercicio:087'))

maior = soma_coluna = soma_pares = 0

matriz = [[0,0,0],[0,0,0],[0,0,0]]
for lin in range(0,3):
    for col in range(0,3):
        matriz[lin][col] = int(input(f'Digite um valor para posição [{lin},{col}]: '))
        if matriz[lin][col] % 2 == 0:
            soma_pares += matriz[lin][col]

print('-++-'* 10)
for lin in range(0,3):
    for col in range(0,3):
        print(f'[{matriz[lin][col]:^5}]',end="")
    print()
print('-++-'* 10)
print(f'A soma dos valores pares é igual: {soma_pares}')
for lin in range(0,3):
    soma_coluna += matriz[lin][2]
print(f'A soma dos valores da terceira coluna = {soma_coluna}')
for col in range(0,3):
    if col == 0:
        maior = matriz[1][col]
    elif matriz[1][col] > maior:
        maior = matriz[1][col]
print(f'O maior valor da segunda linha = {maior}')