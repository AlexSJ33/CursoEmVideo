#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''EX005: Faça um programa que leia um número inteiro e 
mostre na tela seu sucessor e seu antecessor'''

print('\n{:=^30}'.format('Exercicio:005'))
a = int(input('Digite um número: '))



print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(a, a-1, a+1))
