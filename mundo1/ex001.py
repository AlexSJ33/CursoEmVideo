#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#from math import sqrt, floor
#import emoji

#num=int(input('Digite um numero: '))
#raiz = sqrt(num)
#print('A raiz de {} é igual a {:.2f}'.format(num,floor(raiz)))
#print(emoji.emojize("Olá Mundo :earth_americas:", use_aliases=True))
frase='\033[01;31mCurso em Video Python\033[01;33m'
print(frase[15:])
print(len(frase))
print(frase.count('o',0,13))
print(frase.find('o'))
print(frase.find('Alex'))
print('Curso'in frase)
print(frase.replace('Python','Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.split())
print('-'.join(frase))
