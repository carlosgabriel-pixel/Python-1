# Recebendo a quantidade e elementos da lista 1
qtd1 = int(input("Digite a quantidade de elementos da lista 1: "))
print(f"Digite os {qtd1} elementos da lista 1:")
lista1 = [int(input()) for _ in range(qtd1)]

# Recebendo a quantidade e elementos da lista 2
qtd2 = int(input("Digite a quantidade de elementos da lista 2: "))
print(f"Digite os {qtd2} elementos da lista 2:")
lista2 = [int(input()) for _ in range(qtd2)]

lista_intercalada = []
# Descobrir o menor tamanho para intercalar de forma justa até onde for possível
menor_tamanho = min(len(lista1), len(lista2))

# Intercalando os elementos
for i in range(menor_tamanho):
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[i])

# Adicionando os elementos remanescentes da maior lista
if len(lista1) > len(lista2):
    lista_intercalada.extend(lista1[menor_tamanho:])
else:
    lista_intercalada.extend(lista2[menor_tamanho:])

# Imprimindo o resultado final formatado com espaços
print("Lista intercalada:", " ".join(map(str, lista_intercalada)))