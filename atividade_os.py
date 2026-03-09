import subprocess
import os 

def executar_comando(comando):
    try: 
        resultado = subprocess.run(comando, shell=True)
    except Exception as e:
        print("erro ao executar comando")

def limpa_tela(): 
    executar_comando("cls")   

def listar_arquivos(): 
    executar_comando("dir")  

def criar_nova_pasta(): 
    executar_comando("mkdir nova_pasta")    

def criar_arquivo_txt(): 
    executar_comando("type nul > arquivo.txt")

def copia_arquivo_destino():
    executar_comando("copy arquivo.txt destino\\")

def renomiar_arquivo_txt(): 
    executar_comando("ren arquivo.txt novo_nome.txt")

def excluir_arquivo_txt(): 
    executar_comando("del arquivo.txt")

def exibir_informações_windows(): 
    executar_comando("systeminfo")

def ping_site_google(): 
    executar_comando("ping google.com")

def listar_processos(): 
    executar_comando("taklist")

def menu():
    while True:
        print("============|COMANDOS WINDOWS|============")
        print("1 - LIMPAR TELA TERMINAL")
        print("2 - LISTA ARQUIVOS")
        print("3 - CRIAR NOVA PASTA")
        print("4 - CRIAR ARQUIVO DE TEXTO")
        print("5 - COPIA ARQUIVO PARA UMA PASTA")
        print("6 - RENOMIA ARQUIVO TXT")
        print("7 - EXCLUI ARQUIVO TXT")
        print("8 - EXIBE INFORMAÇÕES WINDOWS")
        print("9 - TESTA CONEXÃO GOOGLE")
        print("10 - LISTA PROCESSOS EM EXECUÇÃO")
        print("0 - SAIR")
        print("============|CRIADO POR THIAGO|=============")
        opcao = str(input("escolha:  "))

        match opcao:
            case "1":
                limpa_tela()
            case  "2":
                listar_arquivos()    
            case  "3":
                criar_nova_pasta()    
            case  "4":
                criar_arquivo_txt() 
            case  "5":
                copia_arquivo_destino() 
            case  "6":
                renomiar_arquivo_txt() 
            case  "7":
                excluir_arquivo_txt() 
            case  "8":
                exibir_informações_windows() 
            case  "9":
                ping_site_google() 
            case  "10":
                listar_processos() 
            case  "0":
                print("saindo")
                break
            case _:
                print("eita caba sabidão")
if __name__ == "__main__":
    menu()