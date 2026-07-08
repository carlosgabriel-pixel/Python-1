import random

# Gera aleatoriamente um valor entre 5 e 20 para a quantidade de elementos
num_elementos = random.randint(5, 20)

# Gera a quantidade 'num_elementos' de valores aleatórios entre 1 e 10
elementos = [random.randint(1, 10) for _ in range(num_elementos)]

# Cálculos de soma e média
soma_valores = sum(elementos)
media_valores = soma_valores / num_elementos

# Imprimindo os resultados
print(f"A lista elementos: {elementos}")
print(f"A soma dos valores da lista: {soma_valores}")
print(f"A média dos valores da lista: {media_valores:.2f}")