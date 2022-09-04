#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX097: Faça um programa que tenha uma função chamada escreva(),
que receba um texto qualquer como parâmetro e mostre uma mensagem
com tamanho adaptável."""

print('\n{:=^30}'.format('Exercicio:097'))

def escreva(msg1,msg2,msg3):
    print('-'*len(msg1))
    print(f'{msg1}')
    print('-'*len(msg1))
    print()
    print('-'*len(msg2))
    print(f'{msg2}')
    print('-'*len(msg2))
    print()
    print('-'*len(msg3))
    print(f'{msg3}')
    print('-'*len(msg3))

m1 = str(input('1ª Mensagem: '))
m2 = str(input('2ª Mensagem: '))
m3 = str(input('3ª Mensagem: '))

escreva(m1,m2,m3)
