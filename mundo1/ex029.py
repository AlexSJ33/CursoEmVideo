#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX029: Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele
foi multado.
A multa vai custar R$7,00 por cada Km acima do limite. """

print('\n{:=^30}'.format('Exercicio:029'))
km = float(input('Informe a velocidade atual: ').strip())
dif = km - 80
if km > 80:
    print('Você foi multado em R$ {:.2f} por ter excedido a velociade permitida.'.format(dif * 7))
else:
    print('Velocidade segura')