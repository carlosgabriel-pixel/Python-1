numero = input("Digite o número: ").replace("-", "")

# Se tiver 8 dígitos, adiciona o 9 na frente
if len(numero) == 8:
    numero = "9" + numero

# Formata adicionando o hífen separador de 5 dígitos na frente
numero_formatado = f"{numero[:5]}-{numero[5:]}"

print(f"Número completo: {numero_formatado}")