#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX057: Faça um programa que leia o sexo de uma pessoa,
mas só aceite os valores M ou F.
Caso esteja errado, peça a digitação novamente até ter um
valor correto."""

print('\n{:=^30}'.format('Exercicio:057'))

sexo = str(input('Digite o Sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Informação inválida. Digite o Sexo [M/F]: ')).strip().upper()[0]

if 'M' in sexo:
    print('Sexo Masculino informado, Obrigado!')
else:
    print('Sexo Feminino informado, Obrigado!')