#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX026: Faça um programa que leia uma frase
pelo teclado e mostre:
1- quantas vezes aparece a letra 'A'.
2- em que posição ela aparece a primeira vez.
3- em que posição ela aparece a ultima vez. """

print('\n{:=^30}'.format('Exercicio:026'))
frase = str(input('Digite uma frase: ').upper().strip())
letra = 'A'
print('Letra "A" apareceu {}x'.format(frase.count('A')))
print('Sua primeira posição foi {}'.format(frase.find('A')+1))
print('Sua ultima posição foi {}'.format(frase.rfind('A')+1))