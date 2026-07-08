
import random

# Preenchendo duas listas com 20 valores inteiros aleatórios entre 0 a 50
lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

# Criando a lista de intersecção sem duplicatas e ordenada
intersecao = sorted(list(set(lista1) & set(lista2)))

# Imprimindo as listas e a intersecção
print(f"lista1 = {lista1}")
print(f"lista2 = {lista2}")
print(f"Interseccao = {intersecao}")

# Quantidade de vezes que cada elemento da intersecção aparece em cada lista
print("\nContagem")
for elemento in intersecao:
    qtd_lista1 = lista1.count(elemento)
    qtd_lista2 = lista2.count(elemento)
    print(f"{elemento}: (lista1={qtd_lista1}, lista2={qtd_lista2})")