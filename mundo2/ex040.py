#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX040: Crie um programa que leia duas notas de um aluno
e calcule sua média, mostrando uma mensagem no final, de
acordo com a média atingida:
-Média abaixo de 5.0: REPROVADO
-Média entre 5.0 e 6.9: RECUPERAÇÃO
-Média 7.0 ou superior: APROVADO """

print('\n{:=^30}'.format('Exercicio:040'))
nota1 = float(input('Primeira nota:'))
nota2 = float(input('Segunda nota:'))
media = (nota1+nota2)/2
if media < 5.0:
    print('Média: {:.1f}\nStatus: REPROVADO'.format(media))
elif media >= 5.0 and media < 7.0:
    print('Média: {:.1f}\nStatus: RECUPERAÇÃO'.format(media))
else:
    print('Média: {:.1f}\nStatus: APROVADO'.format(media))