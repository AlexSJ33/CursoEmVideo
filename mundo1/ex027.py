#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX027: Faça um programa que leia o nome
completo de uma pessoa, mostrando em seguida
o primeiro e o último nome separadamente.
Exemplo: Ana Maria de Souza
primeiro:Ana
ultimo: Souza """

print('\n{:=^30}'.format('Exercicio:027'))
nome = str(input('Digite o nome:')).split()
print('Primeiro nome: {}\nUltimo nome: {}'.format(nome[0],nome[-1]))