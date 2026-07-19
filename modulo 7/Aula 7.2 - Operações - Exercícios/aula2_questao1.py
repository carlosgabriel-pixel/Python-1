# Solicita a data de nascimento ao usuário
data = input("Digite uma data de nascimento: ")

# Divide a string nos pontos com '/'
dia, mes, ano = data.split('/')

# Lista com os nomes dos meses (o índice coincide com o número do mês)
meses = [
    "", "Outubro" if mes == "10" else "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]
# Uma abordagem direta com uma lista ordenada:
meses_lista = [
    "", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

nome_mes = meses_lista[int(mes)]

print(f"Você nasceu em {dia} de {nome_mes} de {ano}.")