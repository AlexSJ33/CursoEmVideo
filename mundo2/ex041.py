#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX041: A Confederação Nacional de Natação precisa de um
programa que leia o ano de nascimento de um atleta e
mostre sua categoria, de acordo com a idade:
-Até 9 anos: MIRIM 
-Até 14 anos: INFANTIL
-Até 19 anos: JUNIOR
-Até 20 anos: SÊNIOR
-Acima: MASTER"""

from datetime import date
print('\n{:=^30}'.format('Exercicio:041'))
nasc = int(input('Informe o ano de nascimento:'))
atual = date.today().year
idade = atual - nasc
if idade <= 9:
    print('Idade: {} anos\nCategoria: MIRIM'.format(idade))
elif idade > 9 and idade <= 14:
    print('Idade: {} anos\nCategoria: INFANTIL'.format(idade))
elif idade > 14 and idade <= 19:
    print('Idade: {} anos\nCategoria: JUNIOR'.format(idade))
elif idade > 19 and idade <= 20:
    print('Idade: {} anos\nCategoria: SÊNIOR'.format(idade))
else:
    print('Idade: {} anos\nCategoria: MASTER'.format(idade))