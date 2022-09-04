#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX022: Crie um programa que leia o nome completo de uma pessoa
e mostre: 1- O nome com todas as letras maiúsculas
          2- O nome com todas as letras minúsculas
          3- Quantas letras ao todo(sem considerar espaços)
          4- Quantas letras tem o primeiro nome  """

print('\n{:=^30}'.format('Exercicio:022'))
nome = str(input('Insira o nome completo:'))
ma = nome.upper()
mi = nome.lower()
total_letras = len(nome.replace(" ",""))
dividido = nome.split()
primeiro_nome = len(dividido[0])
print('{}\n{}\n{}\n{}'.format(ma,mi,total_letras,primeiro_nome))