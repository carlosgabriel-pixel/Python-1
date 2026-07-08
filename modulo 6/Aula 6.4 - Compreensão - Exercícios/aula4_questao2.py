frase = input("Digite uma frase: ")

# A lista de vogais da frase, convertidas para minúsculo e ordenadas alfabeticamente
vogais = sorted([char.lower() for char in frase if char.lower() in 'aeiou'])

# A lista de consoantes da frase (mantendo a capitalização original e removendo espaços e pontuações)
consoantes = [char for char in frase if char.isalpha() and char.lower() not in 'aeiou']

print(f"Vogais: {vogais}")
print(f"Consoantes: {consoantes}")