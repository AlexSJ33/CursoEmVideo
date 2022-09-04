#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX072: Crie um programa que tenha uma tupla totalmente
preenchida com uma contagem por extenso, de zero ate vinte.
Seu programa deverá ler um número pelo teclado(entre 0 e 20)
e mostra-lo por extenso."""

print('\n{:=^30}'.format('Exercicio:072'))

numeros = ('zero','um','dois','três','quatro','cinco','seis','sete','oito',
'nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete',
'dezoito','dezenove','vinte')



while True:
    n = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= n <= 20:
        break
    else:
        print('Tente novamente.',end='')
print(f'Você digitou o numero: {numeros[n]}')
