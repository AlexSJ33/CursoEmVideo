#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Crie um script em Python que leia o dia, o mês e o ano de
nascimento de uma pessoa e mostre uma mensagem com a data formatada"""

print('{:=^40}'.format('\033[0;33mDESAFIO 02\033[m'))

d = input("Dia: \033[32m")
m = input("\033[mMês: \033[31m")
a = input("\033[mAno: \033[34m")
print('\033[mVocê nasceu no dia {} de {} de {}. Correto?'.format(d,m,a))
