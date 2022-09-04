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