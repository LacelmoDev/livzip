import zipfile
import os

# Tenta importar rarfile, caso não tenha instalado, o programa avisará
try:
    import rarfile
except ImportError:
    rarfile = None

def verificar_arquivo(nome):
    if not os.path.exists(nome):
        print(f"Erro: O arquivo '{nome}' não foi encontrado.")
        return False
    return True

def criar_zip():
    arquivo_alvo = input("Nome do arquivo/pasta para compactar: ")
    if not verificar_arquivo(arquivo_alvo): return

    nome_zip = input("Nome do arquivo final (sem extensão): ")
    if not nome_zip.endswith('.zip'):
        nome_zip += '.zip'

    try:
        with zipfile.ZipFile(nome_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # arcname serve para o arquivo não levar toda a estrutura de pastas do PC junto
            zipf.write(arquivo_alvo, arcname=os.path.basename(arquivo_alvo))
        print(f"Sucesso! '{nome_zip}' criado.")
    except Exception as e:
        print(f"Ocorreu um erro ao criar o zip: {e}")

def extrair_arquivo():
    arquivo_origem = input("Nome do arquivo para extrair (com extensão): ")
    if not verificar_arquivo(arquivo_origem): return

    destino = "extraido_" + arquivo_origem.split('.')[0]
    
    try:
        # Lógica para ZIP
        if arquivo_origem.lower().endswith('.zip'):
            with zipfile.ZipFile(arquivo_origem, 'r') as zipf:
                zipf.extractall(destino)
            print(f"ZIP extraído na pasta: {destino}")
        
        # Lógica para RAR
        elif arquivo_origem.lower().endswith('.rar'):
            if rarfile is None:
                print("Erro: Biblioteca 'rarfile' não instalada. Use 'pip install rarfile'.")
                return
            with rarfile.RarFile(arquivo_origem, 'r') as rarf:
                rarf.extractall(destino)
            print(f"RAR extraído na pasta: {destino}")
        
        else:
            print("Extensão não suportada para extração.")
            
    except Exception as e:
        print(f"Erro na extração: {e}")

# Menu principal
while True:
    print("\n--- Gerenciador de Arquivos ---")
    opcao = input("Digite 'c' para Compactar (ZIP), 'd' para Descompactar (ZIP/RAR) ou 's' para Sair: ").lower()

    if opcao == 'c':
        criar_zip()
    elif opcao == 'd':
        extrair_arquivo()
    elif opcao == 's':
        break
    else:
        print("Opção inválida!")