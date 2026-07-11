nome = input("Digite seu nome: ")

# O loop vai de 1 até o tamanho total do nome + 1
for i in range(1, len(nome) + 1):
    print(nome[:i])