import random

# 1. Cria a lista com 20 elementos aleatórios entre -10 e 10
lista = [random.randint(-10, 10) for _ in range(20)]

print(f"Original: {lista}")

# 2. Encontrar o intervalo (fatiamento) com a maior quantidade de números negativos consecutivos
maior_qtd_negativos = 0
inicio_melhor_intervalo = 0
fim_melhor_intervalo = 0

# Testamos todas as combinações de fatias possíveis dentro da lista
for i in range(len(lista)):
    for j in range(i + 1, len(lista) + 1):
        fatia = lista[i:j]
        
        # Verifica se TODOS os números nessa fatia específica são negativos
        if all(x < 0 for x in fatia):
            qtd_negativos = len(fatia)
            # Se acharmos uma sequência negativa mais longa, guardamos os índices dela
            if qtd_negativos > maior_qtd_negativos:
                maior_qtd_negativos = qtd_negativos
                inicio_melhor_intervalo = i
                fim_melhor_intervalo = j

# 3. Deleta o intervalo encontrado usando o operador del se alguma sequência foi achada
if maior_qtd_negativos > 0:
    del lista[inicio_melhor_intervalo:fim_melhor_intervalo]

print(f"Editada:  {lista}")