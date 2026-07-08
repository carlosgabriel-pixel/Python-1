lista_original = []

print("Digite os números inteiros. Para parar, digite qualquer caractere não numérico (ex: 'sair').")
print("(Nota: insira pelo menos 4 valores)\n")

# Coleta de dados por loop indefinido
while True:
    entrada = input("Digite um número: ")
    try:
        numero = int(entrada)
        lista_original.append(numero)
    except ValueError:
        # Verifica se o usuário inseriu o mínimo de 4 valores antes de encerrar
        if len(lista_original) < 4:
            print(f"Por favor, insira pelo menos 4 valores. Você inseriu apenas {len(lista_original)}.")
            continue
        break

# Exibição dos resultados utilizando fatiamento (slicing)
print("\n--- Resultados ---")
print(f"A lista original: {lista_original}")
print(f"Os 3 primeiros elementos: {lista_original[:3]}")
print(f"Os 2 últimos elementos: {lista_original[-2:]}")
print(f"A lista invertida: {lista_original[::-1]}")
print(f"Os elementos de índice par: {lista_original[::2]}")
print(f"Os elementos de índice ímpar: {lista_original[1::2]}")