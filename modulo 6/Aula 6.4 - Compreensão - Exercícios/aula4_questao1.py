# 1. Todos os números pares entre 20 e 50 (inclusive)
pares = [x for x in range(20, 51) if x % 2 == 0]

# 2. Os quadrados de todos os valores da lista de 1 a 9
lista_base = [1, 2, 3, 4, 5, 6, 7, 8, 9]
quadrados = [x**2 for x in lista_base]

# 3. Todos os números entre 1 e 100 que sejam divisíveis por 7
divisiveis_por_7 = [x for x in range(1, 101) if x % 7 == 0]

# 4. Para range(0, 30, 3), "par" ou "impar" dependendo da paridade
paridade = ["par" if x % 2 == 0 else "impar" for x in range(0, 30, 3)]

# Demonstrando os resultados:
print("Pares (20 a 50):", pares)
print("Quadrados (1 a 9):", quadrados)
print("Divisíveis por 7 (1 a 100):", divisiveis_por_7)
print("Paridade em range(0, 30, 3):", paridade)