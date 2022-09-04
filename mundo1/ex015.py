#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX015: Escreva um programa que pergunte a quantidade de Km
percorridos por um carro alugado e a quantidade de dias pelos
quais ele foi alugado. Calcule o preço a pagar, sabendo que
o carro custa R$60 por dia e R$0.15 por Km rodado. """

print('\n{:=^30}'.format('Exercicio:015'))
km = float(input('Informe a quantidade em KM, percorrida: '))
dias = int(input('Informe quantos dias de aluguel do veiculo:  '))
total = (dias*60)+(km*0.15)
print('Diária = R$60.00 \nPreço por Km = R$0.15 \nTotal a paga R$ {:.2f}'.format(total))