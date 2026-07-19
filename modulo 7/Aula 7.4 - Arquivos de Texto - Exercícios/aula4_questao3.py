import re

nome_arquivo = "estomago.txt"

with open(nome_arquivo, "r", encoding="utf-8") as f:
    linhas = f.readlines()

# 1. O texto das primeiras 25 linhas
print("--- Primeiras 25 linhas ---")
for i in range(min(25, len(linhas))):
    print(linhas[i].strip('\n'))

print("\n---------------------------\n")

# 2. O número de linhas do arquivo
total_linhas = len(linhas)
print(f"O número de linhas do arquivo: {total_linhas}")

# 3. A linha com maior número de caracteres
linha_longa = max(linhas, key=len).strip('\n')
print(f"A linha com maior número de caracteres possui {len(linha_longa)} caracteres.")

# 4. Contagem dos personagens "Nonato" e "Íria" (palavras inteiras isoladas)
texto_completo = "".join(linhas).lower()

# O uso de \b garante que estamos buscando a palavra exata, ignorando substrings
contagem_nonato = len(re.findall(r'\bnonato\b', texto_completo))
contagem_iria = len(re.findall(r'\bíria\b', texto_completo))

print(f"Número de menções a 'Nonato': {contagem_nonato}")
print(f"Número de menções a 'Íria': {contagem_iria}")