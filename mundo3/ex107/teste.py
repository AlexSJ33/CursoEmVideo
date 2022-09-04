#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX107: Crie um módulo chamado moeda.py que tenha as funções
incorporadas aumentar(),diminuir(),dobro() e metade().
Faça também um programa que importe esse módulo e use algumas
dessas funções."""
#--Exemplo:
#--Digite o preço: R$
#--A metade de 500.0 é 250.0
#--O dobro de 500.0 é 1000.0
#--Aumentando 10%, temos 550.0
#--Reduzindo 13%, temos 435.0

print('\n{:=^30}'.format('Exercicio:107'))
import moeda

num = float(input('Digite o preço: R$'))
print(f'A metade de R${num} é R${moeda.metade(num)}')
print(f'O dobro de R${num} é R${moeda.dobro(num)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(num,10)}')
print(f'Reduzindo 13%, temos R${moeda.diminuir(num,13)}')