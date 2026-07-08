alunos = ["Maria", "Jose", "Carla", "Sol"]
notas = [35, 50, 20, 80]

# Nova construção utilizando compreensão de listas baseada no índice para filtrar os aprovados
aprovados = [alunos[i] for i in range(len(notas)) if notas[i] >= 60]

print(aprovados)