import os

# Solicita a frase ao usuário
frase = input("Digite uma frase: ")

nome_arquivo = "frase.txt"

# Salva a frase no arquivo de texto
with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.write(frase)

# Obtém e imprime o caminho completo absoluto do arquivo
caminho_completo = os.path.abspath(nome_arquivo)
print(f"Frase salva em {caminho_completo}")