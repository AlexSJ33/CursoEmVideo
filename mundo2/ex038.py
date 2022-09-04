#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX038: Escreva um programa que leia dois números inteiros
e compare-os, mostrando na tela uma mensagem:
-O primeiro valor é MAIOR
-O segundo valor é MAIOR
-Não existe valor maior, os dois são iguais."""

print('\n{:=^30}'.format('Exercicio:038'))
num1 = int(input('Digite o primeiro numero:'))
num2 = int(input('Digite o segundo numero:'))
if num1 > num2:
    print('O primeiro valor é MAIOR')
elif num2 > num1:
    print('O segundo valor é MAIOR')
else:
    print('Não existe valor maior, os dois são iguais.')