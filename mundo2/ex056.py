#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX056: Desenvolva um programa que leia o nome,
idade e sexo de 4 pessoas. No final do programa mostre:
- A media de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres tem menos de 20 anos."""

print('\n{:=^30}'.format('Exercicio:056'))
import sys
soma_idade = 0
mais_velho = 0
nome_velho = ''
mulher = 0
feminino = False
for p in range(1,5):
    print('----- {}ª PESSOA -----'.format(p))
    try:
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        sexo = str(input('Sexo [M/F]: ').upper())
    except ValueError:
        print('Informação invalida')
        sys.exit()
        
    soma_idade +=idade
    media = (soma_idade / p)

    if sexo == 'M':
        if (p == 1):    
            mais_velho = idade
            nome_velho = nome
        else:
            if idade > mais_velho:
                mais_velho = idade
                nome_velho = nome
    elif sexo == 'F':
        feminino = True
        if idade < 20:
            mulher = mulher +1
    else:
        print('Digite "M" para Masculino ou "F" para Feminino.')
        sys.exit()
print('--'*20)
print('A media de idade do grupo é {} anos'.format(media))
if mais_velho == 0:
    print('Não consta homens na lista')
else:
    print('O homem mais velho tem {} anos e se chama {}'.format(mais_velho,nome_velho))
if feminino == False:
    print('Não consta mulheres na lista')
elif (feminino == True) and (mulher == 0):
    print('Não consta mulheres menores de 20 anos')
else:
    print('{} Mulher(es) tem idade menor que 20 anos'.format(mulher))