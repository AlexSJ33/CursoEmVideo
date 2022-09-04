import sys

dic_cad = dict()
def leiaInt(num):
    while True:
        try:
            n = int(input(num))
        except (ValueError, TypeError):
            print('\033[0;33mERRO! Digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompida pelo usuario.\033[m')
            break
        if n < 1 or n > 3:
            print('\033[0;33mDigite um valor referente as opções.\033[m')
            continue
        else:
            break
    return n

def leiaNome(nome):
    while True:
        try:
            dic_cad['nome'] = str(input(nome))
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompida pelo usuario.\033[m')
            sys.exit()     
        if (dic_cad['nome'] == ''):
            print('\033[0;33mERRO! Necessario inserir um <NOME>.\033[m')
            continue
        elif dic_cad['nome'].strip().isnumeric():
            print('\033[0;33mERRO! Não é permitido numeros no campo <NOME>.\033[m')
            continue
        return dic_cad['nome']
    
def leiaIdade(idade):
    while True:
        try:
            dic_cad['idade'] = int(input(idade))
        except (ValueError, TypeError):
            print('\033[0;33mERRO! Digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompida pelo usuario.\033[m')
            sys.exit()
        return dic_cad['idade']
