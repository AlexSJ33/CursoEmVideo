#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX025: Crie um programa que leia o nome de uma
pessoa e diga se ela tem 'SILVA' no nome. """

print('\n{:=^30}'.format('Exercicio:025'))
pessoa = str(input('Digite o nome completo:').upper().strip())
if 'SILVA' in pessoa:
    print('SILVA encontrado!!')
else:
    print('Não tem SILVA no nome!!')