#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX112: Dentro do pacote utilidadesCeV que criamos
no desafio 111, temos um módulo chamado dado. Crie uma
função chamada leiaDinheiro() que seja capaz de funcionar
como a função input(), mas com uma validação de dados
para aceitar apenas valores que sejam monetários."""

print('\n{:=^30}'.format('Exercicio:112'))

from utilidadescev import dado, moeda

num = dado.validador('Digite o preço: R$')
moeda.resumo(num, 12,3)