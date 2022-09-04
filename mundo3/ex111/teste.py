#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX111: Crie um pacote chamado utilidadesCeV
que tenha dois módulos internos chamados moeda e dado.
Transfira todas as funções utilizadas nos desafios 107,
108,109 e 110 para o primeiro pacote e mantenha tudo funcionando."""
#--Exemplo:
#--Digite o preço: R$500
#---------------------------
#     RESUMO DO VALOR
#---------------------------
# Preço analisado: R$500,00
# Dobro do preço:  R$1000,00
# Metade do preço: R$250,00
# 80% de aumento:  R$900,00
# 35% de redução:  R$325,00
#---------------------------

print('\n{:=^30}'.format('Exercicio:111'))

from utilidadescev import moeda

num = float(input('Digite o preço: R$'))
moeda.resumo(num, 12,3)