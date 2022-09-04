#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX036: Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa. O programa vai perguntar o valor da
casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode
exceder 30% do salário ou então o empréstimo será negado. """

from datetime import date
print('\n{:=^30}'.format('Exercicio:036'))
print('#    \033[1;34mMINHA CASA MINHA VIDA\033[m   #')
print('#'*30,'\n')
nome=str(input('Digite seu nome:')).strip()
imovel=float(input('Por favor informe o valor do imóvel: R$ '))
salario=float(input('Qual salário atual? R$ '))
tempo=int(input('Em quantos ANOS pretende quitar seu imóvel? '))
meses = tempo * 12
prestacao = imovel / meses
limite = salario * 0.30
ano= (date.today().year + tempo)
print('-='*20)
print('Valor do Imóvel: R${:.2f}'.format(imovel))
print('Renda Familiar: R${:.2f}'.format(salario))
print('Tempo de Financiamento: {} Ano(s)'.format(tempo))
print('Prestação: {} parcelas de R${:.2f}'.format(meses,prestacao))
if prestacao > limite:
    print('Emprestimo:\033[0;31mNegado\033[m')
else:
    print('Empréstimo:\033[0;33mLiberado\033[m')
    print('Parabéns! Você quitará sua dívida em {}'.format(ano))


