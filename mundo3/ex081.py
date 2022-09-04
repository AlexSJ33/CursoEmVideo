#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX081: Crie um programa que vai ler varios
numeros e colocar em uma lista.
Depois disso, mostre:
A) Quantos numeros foram digitados.
B) A lista de valores ordenada de forma Decrescente.
C) Se o valor 5 foi digitado e está ou não na lista."""

print('\n{:=^30}'.format('Exercicio:081'))

valores = []
while True:
    valores.append(int(input('Digite o valor: ')))
    res = str(input('Deseja continuar? [S/N]'))
    if res in 'Nn':
        break
ordem = valores[:]
ordem.sort(reverse = True)
print(f'Foram digitados {len(valores)} numeros.')
print(f'Ordem Decrescente: {ordem}.')
if 5 in valores:
    print(f'O valor 5 foi digitado e está na {valores.index(5)+1}ª posição ')
else:
    print('O valor 5 não foi digitado.')