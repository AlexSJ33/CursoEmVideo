#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX101: Crie um programa que tenha uma função chamada voto() que
vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem o voto
NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições"""
#Exemplo:
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Em que ano você nasceu? 2000
# Com 18 anos: VOTO OBRIGATÓRIO.
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Em que ano você nasceu? 2010
# Com 8 anos: NÃO VOTA.
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Em que ano você nasceu? 1970
# Com 48 anos: VOTO OBRIGATÓRIO.
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# Obs: mais de 65 anos
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Em que ano você nasceu? 1910
# Com 108 anos: VOTO OPCIONAL.
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
print('\n{:=^30}'.format('Exercicio:101'))

from datetime import date

def voto(ano=0):
    hoje = date.today().year
    ano = hoje - nasc
    if ano >= 18 and ano < 65:
        return f'Com {ano} anos: VOTO OBRIGATÓRIO'
    elif ano < 18:
        return f'Com {ano} anos: NÃO VOTA'
    else:
        return f'Com {ano} anos: VOTO OPCIONAL'

#Programa princial
print('--'*15)
nasc = int(input('Em que ano você nasceu? '))
print(voto())
print('--'*15)