#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX115: Crie um pequeno sistema modularizado que permita cadastrar
pessoas pelo seu nome e idade em um arquivo de texto simples.
O Sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas
as pessoas cadastradas e opção SAIR. (3 opçoes)"""

#---------------------------------
#         MENU PRINCIPAL
#---------------------------------
# 1 - Ver pessoas cadastradas
# 2 - Cadastrar nova Pessoa
# 3 - Sair do Sistema
#---------------------------------
# Sua Opção:
from utilidadescev import validador
from utilidadescev import cadastro


print('\n{:=^35}'.format('Exercicio:115'))

print('-'*35)
print('MENU PRINCIPAL'.center(35))
print('-'*35)
print('\033[1;33m1\033[m','-','\033[1;34mVer pessoas cadastradas\033[m')
print('\033[1;33m2\033[m','-','\033[1;34mCadastrar nova Pessoa\033[m')
print('\033[1;33m3\033[m','-','\033[1;34mSair do Sistema\033[m')
print('-'*35)
n=validador.leiaInt('\033[0;36mSua Opção: \033[m') # Tratar entrada de dados
print('-'*35)
if n == 1:
    cadastro.consulta()
elif n == 2:
    print('-'*35, '\033[1;33m')
    print('CADASTRO'.center(35),'\033[m')
    print('-'*35)
    p=validador.leiaNome('Nome: \033[3;32m')
    i=validador.leiaIdade('\033[mIdade: \033[3;32m')
    cadastro.novo()
elif n == 3:
    cadastro.sair()

print(f'{validador.dic_cad}\033[m')

