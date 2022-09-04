#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX019: Um professor quer sortear um dos seus quatro
alunos para apagar o quadro. Faça um programa que ajude ele
lendo o nome deles e escrevendo o nome do escolhido """
from random import choice
print('\n{:=^30}'.format('Exercicio:019'))
lista = []
lista.append(input('Primeiro Aluno: '))
lista.append(input('Segundo Aluno: '))
lista.append(input('Terceiro Aluno: '))
lista.append(input('Quarto Aluno: '))
escolhido = choice(lista)
print('O Aluno escolhido foi {}'.format(escolhido))