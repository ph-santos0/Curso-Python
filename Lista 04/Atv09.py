nome_arquivo = input("Digite o nome do arquivo (ex: teste.txt): ")

try:
    arquivo = open(nome_arquivo, "r") 
    print("Arquivo encontrado e aberto com sucesso.")
    arquivo.close()

except FileNotFoundError:
    print("Arquivo não encontrado. Verifique o nome e tente novamente.")

print("O programa continua sem encerrar bruscamente.")