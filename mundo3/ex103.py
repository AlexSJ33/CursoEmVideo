#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX103: Faça um programa que tenha uma função
chamada ficha(), que receba dois parâmetros opcionais;
o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador,
mesmo que algum dado não tenha sido informado corretamente"""
#Exemplo:
# ------------------------------------------------
# Nome do Jogador: Romario
# Número de Gols: 33
# O jogador Romario fez 33 gol(s) no campeonato.
# ------------------------------------------------
# Nome do Jogador: 
# Número de Gols: 2
# O jogador <desconhecido> fez 2 gol(s) no campeonato.
# ------------------------------------------------
# Nome do Jogador: 
# Número de Gols: 
# O jogador <desconhecido> fez 0 gol(s) no campeonato.
# ------------------------------------------------
print('\n{:=^30}'.format('Exercicio:103'))

def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


#PROGRAMA PRINCIPAL
jogador = str(input('Nome do Jogador: '))
numero_gols = str(input('Número de Gols: '))
if numero_gols.isnumeric():
    numero_gols = int(numero_gols)
else:
    numero_gols = 0
if jogador.strip() =='':   
    ficha(gols=numero_gols)
else:
    ficha(jogador,numero_gols)