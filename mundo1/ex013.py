#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX013: Faça um algoritimo que leia o salário de um funcionário
        e mostre seu novo salário, com 15 porcento de aumento."""

print('\n{:=^30}'.format('Exercicio:013'))
salario = float(input('Salário atual R$: '))
reajuste = salario*0.15
print('Reajuste salarial de 15%')
print('TOTAL R${:.2f}'.format(salario+reajuste))

