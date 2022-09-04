#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX037: Escreva um programa que leia um número inteiro
qualquer e peça para o usuário escolher qual será a base de conversão:
-1 para binário
-2 para octal
-3 para hexadecimal """

print('\n{:=^30}'.format('Exercicio:037'))
num = int(input('Insira um numero: '))
print('-='*15)
print('1 - binário\n2 - octal\n3 - hexadecimal')
binario=format(num,"b")
octal=format(num,"o")
hexa=format(num,"x")
conversao=int(input('Escolha uma conversão:'))

if conversao == 1:
    print(binario)
elif conversao == 2:
    print(octal)
else:
    print(hexa)