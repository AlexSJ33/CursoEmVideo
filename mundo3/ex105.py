#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX105: Faça um programa que tenha uma função notas() que
pode receber várias notas de alunos e vai retornar um dicionário
com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
OBS: Adicione também as docstrings da função"""
#Exemplo:
# ------------------------------------------------
# Programa principal
# resp = notas(5.5, 9.5, 10, 6.5')
# print(resp)
# ------------------------------------------------
# {'total': 4, 'maior': 10, 'menor': 5.5, 'média': 7.875}
# ------------------------------------------------
# resp = notas(5.5, 9.5, 10, 6.5, sit=True')
# print(resp)
# ------------------------------------------------
# {'total': 4, 'maior': 10, 'menor': 5.5, 'média': 7.875, 'situação': 'BOA'}
# help(notas)
# notas(*n,sit=False)
# --> Função para analisar notas e situações de vários alunos.
# :param n: uma ou mais notas dos alunos (aceita várias)
# :param sit: valor opcional, indicando se deve ou não adicionar a situação
# :return: dicionário com várias informações sobre a situação da turma.
# -----------------------------------------------------------------------
print('\n{:=^30}'.format('Exercicio:105'))

def notas(*n,sit=False):
    """ #--DOCSTRINGS--#
    notas(*n,sit=False)
    --> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma."""
    t = dict()
    t['total'] = (len(n))
    t['maior'] = (max(n))
    t['menor'] = (min(n))
    t['média'] = (sum(n)/len(n))
    if sit:
        if t['média'] > 7:
            t['situação'] = 'BOA'
        elif t['média'] > 5 <= 7:
            t['situação'] = 'RAZOÁVEL'
        else:
            t['situação'] = 'RUIM'
    print('-'*len(str(t)))
    return t

# PROGRAMA PRINCIAL
resp = notas(5.5, 6.5, 7, 6.5,sit=True)
print(resp)
print('-'*len(str(resp)))
help(notas)