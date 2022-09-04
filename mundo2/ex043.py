#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX043: Desenvolva uma lógica que leia o peso e a 
altura de uma pessoa, calcule o seu IMC e mostre
seu status, de acordo com a tabela abaixo:
-Abaixo de 18.5: Abaixo do Peso
-Entre 18.5 e 25: Peso ideal
-25 até 30: Sobrepeso
-30 até 40: Obesidade
-Acima de 40: Obesidade mórbida"""

print('\n{:=^30}'.format('Exercicio:043'))
print('#{:^38}#'.format('\033[1;35mCalculadora IMC\033[m'))
print('#'*30,'\n')
peso=float(input('Qual seu peso? '))
altura=float(input('Qual a sua altura? '))
imc= peso/(altura**2)
print('PESO: {}\nALTURA: {}\nIMC: {:.2f} kg/m2'.format(peso,altura,imc))
if imc >= 18.5 and imc < 25.01:
    print('Status: Peso ideal')
elif imc > 25 and imc < 30.01:
    print('Status: Sobrepeso')
elif imc > 30 and imc < 40.01:
    print('Status: Obesidade')
elif imc < 18.5:
    print('Status: Abaixo do Peso')
else:
    print('Status: Obesidade mórbida')