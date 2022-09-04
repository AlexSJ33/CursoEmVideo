#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX108: Adapte o código do desafio 107, criando uma função
adicional chamada moeda() que consiga mostrar os valores como
um valor monetário formatado."""
#--Exemplo:
#--Digite o preço: R$
#--A metade de R$500,00 é R$250,00
#--O dobro de R$500,00 é R$1000,00
#--Aumentando 10%, temos R$550,00

print('\n{:=^30}'.format('Exercicio:108'))

import moeda

num = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(num,10))}')
print(f'Reduzindo 13%, temos {moeda.moeda(moeda.diminuir(num,13))}')
print()