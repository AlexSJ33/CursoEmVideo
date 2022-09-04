#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX083: Crie uma programa onde o usuario
digite uma expressão qualquer que use parenteses.
Seu aplicativo deverá analizar se a expressão passada
esta com os parenteses abertos e fechados na ordem correta."""

print('\n{:=^30}'.format('Exercicio:083'))

expr = str(input('Digite sua expressão:'))
parenteses = []
for simbolo in expr:
    if simbolo == '(':
        parenteses.append('(')
    elif simbolo == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(')')
            break
if len(parenteses )== 0:
    print('Expressão válida.')
else:
    print('Expressão inválida.')