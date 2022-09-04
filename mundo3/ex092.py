#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX092: Crie um programa que leia nome, ano de nascimento
e carteira de trabalho e cadastre-os (com idade) em um
dicionário se por acaso a CTPS for diferente de ZERO, o
dicionário recebera também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a 
pessoa vai se aposentar."""

from datetime import date
print('\n{:=^30}'.format('Exercicio:092'))

worker = dict()

worker['name'] = str(input('Name: '))
worker['year'] = int(input('Year of birth: '))
worker['card'] = int(input('Work card (0 does not have): '))
today = date.today().year

while worker['card'] > 0:
    worker['contract'] = int(input('Year of contract: '))
    worker['salary'] = int(input('Salary U$: '))

    print('-=-'*12)  
    worker['age'] = today - worker['year']
    retirement = ((worker['contract'] + 35) - worker['year'])
    del worker['year']
    
    print(worker)
    print(f'Name has the value: {worker["name"]}')
    print(f'Age has the value: {worker["age"]}')
    print(f'Work card has the value: {worker["card"]}')
    print(f'Contract has the value: {worker["contract"]}')
    print(f'Retirement has the value: {retirement}')
    break

else: 

    print('-=-'*12)  
    worker['age'] = today - worker['year']
    del worker['year']
    print(worker)
    print(f'Name has the value: {worker["name"]}')
    print(f'Age has the value: {worker["age"]}')
    print(f'Work card has the value: {worker["card"]}')
