#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX020: O mesmo professor do desafio anterior quer 
sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.  """

from random import shuffle
print('\n{:=^30}'.format('Exercicio:020'))

lista = []
lista.append(input('Primeiro Aluno: '))
lista.append(input('Segundo Aluno: '))
lista.append(input('Terceiro Aluno: '))
lista.append(input('Quarto Aluno: '))
shuffle(lista)
print('Ordem de apresentação:\n {}'.format(lista))