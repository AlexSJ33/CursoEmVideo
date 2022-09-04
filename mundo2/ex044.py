#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX044: Elabore um programa que calcule o valor a ser
pago por um produto, considerando o seu preço normal
e condição de pagamento:
-Á vista dinheiro/cheque: 10% de desconto.
-Á vista no cartão: 5% de desconto.
-Em até 2x no cartão: preço normal
-3x ou mais no cartão: 20% de juros"""

print('\n{:=^30}'.format('Exercicio:044'))
try:
    produto = float(input('Preço do Produto: '))
    desc10 = produto - (produto*0.10)
    desc5 = produto - (produto*0.05)
    cartao3x = produto + (produto*0.20)
    print('-'*30)
    print('Qual a forma de pagamento?\n')
    print('1 - Á vista dinheiro/cheque\n2 - Á vista no cartão\n3 - Em até 2x no cartão\n4 - 3x ou mais no cartão')
    opt=int(input('Opção: '))
    if opt == 1:
        print('Á vista dinheiro/cheque tem 10% de desconto')
        print('Total a pagar R${:.2f}'.format(desc10))
    elif opt == 2:
        print('Á vista no cartão de credito tem 5% de desconto')
        print('Total a pagar R${:.2f}'.format(desc5))
    elif opt == 3:
        parcela = produto / 2
        print('Sua compra será parcelada em 2x de R${} SEM JUROS'.format(parcela))
        print('Total a pagar R${:.2f}'.format(produto))
    elif opt == 4:
        total_parcela = int(input('Quantas parcelas? '))
        parcela = cartao3x / total_parcela
        print('Sua compra será parcela em {}x  de {:.2f} COM JUROS'.format(total_parcela, parcela))
        print('Total a pagar R${:.2f}'.format(cartao3x))
    else:
        print('Não existe essa opção..\nFim do programa!')
except ValueError:
    print('Digite apenas numero!\n')
