#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX034: Escreva um programa que pergunte o salario
de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00 calcule
um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%. """

print('\n{:=^30}'.format('Exercicio:034'))
salario = float(input('Qual salario do funcionario? R$'))
if salario > 1250.00:
    aumento = ((salario * 0.10) + salario)
    print('Seu aumento foi de 10%')
else:
    aumento = ((salario * 0.15) + salario)
    print('Seu aumento foi de 15%')
print('Salario reajustado para R${:.2f}'.format(aumento))

