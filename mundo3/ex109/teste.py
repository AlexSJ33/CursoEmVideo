#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX109: Modifique as funções que foram criadas no desafio 107
para que elas aceitem um parametro a mais, informando se o valor
retornado por elas vai ser ou não formatado pela função moeda(),
desenvolvida no desafio 108."""
#--Exemplo:
#--Digite o preço: R$
#--A metade de R$500,00 é R$250,00 - True / False
#--O dobro de R$500,00 é R$1000,00 - True / False
#--Aumentando 10%, temos R$550,00  - True / False


print('\n{:=^30}'.format('Exercicio:109'))

import moeda

num = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(num)} é {moeda.metade(num, True)}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(num,10, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(num,13, True)}')
print()