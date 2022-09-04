#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX102: Crie um programa que tenha a função fatorial() que 
receba dois parâmetros: o primeiro que indique o número a calcular
e o outro chamado show, que será um valor lógico (opcional) indicando
se será mostrado ou não na tela o processo de cálculo do fatorial."""
#Exemplo:
# help(fatorial)
# fatorial(n,show=False)
# --> Calcula o Fatorial de um número.
# :param n: O número a ser calculado.
# :param shown: (opcional) Mostrar ou não a conta.
# :return: O valor do Fatorial de um número n.
# ------------------------------------------------
# Saida:
# print(fatorial(5, show=True))
#---------------------------
# 5 x 4 x 3 x 2 x 1 = 120
#---------------------------
print('\n{:=^30}'.format('Exercicio:102'))
def fatorial(n, show=False):
    """
    --> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    num = 1
    print('-'*30)
    while n >= 1:
        num = num * n
        n -=1
        if show == True:
            if n >= 1:
                print(n+1, 'x',end=' ')
            else:
                print(n+1, '=',end=' ')
        else:
            continue      
    return num
#--> Programa principal    
print(fatorial(5,show=True))
print('-'*30)
#print(help(fatorial))