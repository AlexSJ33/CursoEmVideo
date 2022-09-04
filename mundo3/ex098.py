#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX098: Faça um programa que tenha uma função chamada
contador(), que receba tres parâmetros: inicio,fim, e passo
e realize a contagem.
Seu programa tem que realizar tres contagens atraves da função criada:
a) De 1 ate 10, de 1 em 1
b) De 10 ate 0, de 2 em 2
c) Uma contagem personalizada."""

#Exemplo:
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#Contagem de 1 ate 10 de 1 em 1
#1 2 3 4 5 6 7 8 9 10 FIM!
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#Contagem de 10 ate 0 de 2 em 2
#1 2 3 4 5 6 7 8 9 10 FIM!
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#Agora é sua vez de persolanizar a contagem!
#Inicio: 10
#Fim:    100
#Passo:  8
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#Contagem de 10 ate 100 de 8 em 8
#10 18 26 34 42 50 58 66 74 82 90 98 FIM!
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

print('\n{:=^30}'.format('Exercicio:098'))

from time import sleep

def contador(inicio,fim,passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1

    print('--'*15)
    print(f'Contagem de {inicio} ate {fim} de {passo} em {passo}')
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(cont,end=' ',flush=True)
            sleep(0.5)
            cont += passo
        print('FIM!')
    else:
        cont = inicio
        sleep(2)
        while cont >= fim:
            print(cont, end=' ',flush=True)
            sleep(0.5)
            cont -= passo
        print('FIM!')
        print('--'*15)

contador(1,10,1)
contador(10,0,2)
print('Agora é a sua vez! Personalise a sua contagem')
ini = int(input('INICIO:  '))
fim = int(input('FIM:     '))
pas = int(input('PASSO:   '))
contador(ini,fim,pas)
print()