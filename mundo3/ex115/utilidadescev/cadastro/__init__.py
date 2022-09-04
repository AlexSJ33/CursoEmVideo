from utilidadescev import validador
import sys

def consulta():
    try:
        with open('cadastro.txt','r') as arquivo:
            for linha in arquivo.readlines():
                print(linha.split(':')[1])
                
    except (FileNotFoundError):
        print('\033[31mNenhum dado encontrado, sistema encerrado...\033[m')
        sys.exit()
        
def novo():
    
    with open('cadastro.txt','a+') as arquivo:
            arquivo.write(str(validador.dic_cad)+'\n')
   

def sair():
    print(' '*6,'\033[3;35mObrigado e até Logo!\033[m')
    print('-'*35)
    sys.exit()

