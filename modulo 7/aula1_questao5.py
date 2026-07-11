frase = input("Digite uma frase: ")
vogais_permitidas = "aeiouAEIOU"

lista_indices = []
total_vogais = 0

for indice, letra in enumerate(frase):
    if letra in vogais_permitidas:
        total_vogais += 1
        lista_indices.append(indice)

print(f"{total_vogais} vogais")
print(f"Índices {lista_indices}")