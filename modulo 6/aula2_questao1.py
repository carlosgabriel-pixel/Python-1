import random

# Gerando 20 valores inteiros aleatórios entre -100 e 100
lista_original = [random.randint(-100, 100) for _ in range(20)]

# Criando a lista ordenada sem modificar a original
lista_ordenada = sorted(lista_original)

# Encontrando os índices do maior e do menor valor na lista original
indice_maior = lista_original.index(max(lista_original))
indice_menor = lista_original.index(min(lista_original))

# Imprimindo os resultados na ordem estabelecida
print("A lista ordenada, sem modificar a lista original:")
print(lista_ordenada)
print("\nA lista original:")
print(lista_original)
print(f"\nO índice do maior valor da lista: {indice_maior}")
print(f"O índice do menor valor da lista: {indice_menor}")