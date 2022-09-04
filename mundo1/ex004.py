#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''EX004: Faça um programa que leia algo pelo teclado e mostre na tela 
o seu tipo primitivo e todas as informações possíveis sobre ele.'''

print('\n{:=^30}'.format('Exercicio:004'))
n = input('Digite alguma coisa: ')
print('\nO Tipo primitivo desse valor é:',type(n))
print('É um número? ',n.isnumeric())
print('É alfabético? ',n.isalpha())
print('É alfanumérico? ',n.isalnum())
print('Está em maíusculas? ',n.isupper())
print('Está em minúsculas? ',n.islower())
print('Só tem espaços? ',n.isspace())
print('Está capitalizado? ',n.istitle())