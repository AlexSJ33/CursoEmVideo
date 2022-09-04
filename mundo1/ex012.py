#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX012: Faça um algoritimo que leia o preço de um produto e mostre seu
        novo preço, com 5 porcento de desconto."""

print('\n{:=^30}'.format('Exercicio:012'))
produto = float(input('Valor do Produto: '))
desconto = produto *0.95
print('Produto com desconto de 5%')
print('Novo preço = {:.2f}'.format(desconto))
