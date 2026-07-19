frase = input("Digite uma frase: ")
frase_modificada = ""

vogais = "aeiouAEIOU"

for caractere in frase:
    if caractere in vogais:
        frase_modificada += "*"
    else:
        frase_modificada += caractere

print(f"Frase modificada: {frase_modificada}")