frase = input("Digite uma frase: ")
palavra_alvo = input("Digite a palavra objetivo: ").lower()

# Limpa pontuações básicas e quebra a frase em uma lista de palavras
palavras_da_frase = frase.replace(",", "").replace(".", "").split()
anagramas_encontrados = []

# Ordena as letras da palavra objetivo para comparação rápida
alvo_ordenado = sorted(palavra_alvo)

for palavra in palavras_da_frase:
    # Compara a versão minúscula e ordenada
    if sorted(palavra.lower()) == alvo_ordenado:
        anagramas_encontrados.append(palavra)

print(f"Anagramas: {anagramas_encontrados}")