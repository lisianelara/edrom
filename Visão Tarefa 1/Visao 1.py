import os
import glob
import shutil

def tarefa_visao(caminho_pasta):
    # Criar uma nova pasta para armazenar os arquivos alterados
    nova_pasta = os.path.join(caminho_pasta, 'pasta2')
    os.makedirs(nova_pasta, exist_ok=True)

    # Lista todos os arquivos .txt na pasta
    arquivos_txt = glob.glob(os.path.join(caminho_pasta, '*.txt'))

    for caminho_arquivo_entrada in arquivos_txt:
        # Ler o conteúdo do arquivo de entrada
        with open(caminho_arquivo_entrada, 'r') as arquivo_entrada:
            linhas = arquivo_entrada.readlines()

        # Alterar o índice inicial de 0 para 1
        linhas = [linha.replace('0 ', '1 ') for linha in linhas]

        # Construir caminho completo para o arquivo de saída
        nome_arquivo = os.path.basename(caminho_arquivo_entrada).replace('train_', 'ball_')
        caminho_arquivo_saida = os.path.join(nova_pasta, nome_arquivo)

        # Escrever as alterações no arquivo de saída
        with open(caminho_arquivo_saida, 'w') as arquivo_saida:
            arquivo_saida.writelines(linhas)

# Exemplo de uso
caminho_pasta = '/caminho/para/pasta1'
tarefa_visao(caminho_pasta)
