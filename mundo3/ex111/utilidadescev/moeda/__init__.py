def aumentar(preço = 0, taxa = 0, formatado=False):
    resultado = preço + (preço * taxa/100)
    return resultado if not formatado else moeda(resultado)

def diminuir(preço = 0, taxa = 0, formatado=False):
    resultado = preço - (preço * taxa/100)
    return resultado if not formatado else moeda(resultado)
    
def dobro(preço = 0, formatado=False):
    resultado = preço * 2
    return resultado if not formatado else moeda(resultado)

def metade(preço = 0, formatado=False):
    resultado = preço / 2
    return resultado if not formatado else moeda(resultado)

def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')

def resumo(preço = 0, taxa_aum=10, taxa_redu=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxa_aum}% de aumento: \t{aumentar(preço, taxa_aum, True)}')
    print(f'{taxa_redu}% de redução: \t\t{diminuir(preço, taxa_redu,True)}')
    print('-'*30)