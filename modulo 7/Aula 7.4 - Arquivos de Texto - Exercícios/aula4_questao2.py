import re

# Lê o conteúdo do exercício anterior
with open("frase.txt", "r", encoding="utf-8") as arquivo_origem:
    conteudo = arquivo_origem.read()

# Substitui tudo o que não for letra ou espaço por nada, mantendo os acentos
# O regex '[^\w\s]' remove pontuações, e removemos números manualmente ou via lógica
palavras_limpas = []
for palavra in conteudo.split():
    # Mantém apenas caracteres alfabéticos da palavra
    palavra_filtrada = "".join(c for c in palavra if c.isalpha())
    if palavra_filtrada:
        palavras_limpas.append(palavra_filtrada)

# Grava cada palavra em uma nova linha no arquivo palavras.txt
with open("palavras.txt", "w", encoding="utf-8") as arquivo_destino:
    for palavra in palavras_limpas:
        arquivo_destino.write(palavra + "\n")

# Imprime o conteúdo final salvo para validação
print("Conteúdo do arquivo 'palavras.txt':\n")
with open("palavras.txt", "r", encoding="utf-8") as arquivo_leitura:
    print(arquivo_leitura.read())