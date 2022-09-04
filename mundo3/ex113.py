#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX113: Reescreva a função leiaInt() que fizemos no desafio 104,
incluindo agora a possibilidade da digitação de um número de tipo
inválido. Aproveite e crie também uma função leiaFloat() com a
mesma funcionalidade."""


print('\n{:=^30}'.format('Exercicio:113'))

def leiaInt(num):
    while True:
        try:
            n = int(input(num))
        except (ValueError, TypeError):
            print('\033[0;33mERRO! Digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompida pelo usuario.\033[m')
            return 0
        else:
            return n
        
def leiaFloat(num):
    while True:
        try:
            n = float(input(num))
        except (ValueError, TypeError):
            print('\033[0;33mERRO! Digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompida pelo usuario.\033[m')
            return 0
        else:
            return n

#PROGRAMA PRINCIPAL
n1 = leiaInt('Digite um número Inteiro: ')
n2 = leiaFloat('Digite um número Real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')