# Programa para calcular a média de idade dos respondentes
N = int(input())
soma_idades = 0

for i in range(N):
    idade = int(input())
    soma_idades += idade

media = soma_idades / N
print(media)