#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX110: Adicione ao módulo moeda.py criado nos desafios
anteriores, uma função chamada resumo(), que mostre na
tela algumas informações geradas pelas funções que já 
temos no módulo criado até aqui."""
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

print('\n{:=^30}'.format('Exercicio:110'))

import moeda

num = float(input('Digite o preço: R$'))
moeda.resumo(num)