while True:
    entrada = input("Digite uma frase (digite \"fim\" para encerrar): ")
    
    # Condição de parada
    if entrada.lower() == "fim":
        break
        
    # Limpeza da frase: mantém apenas letras e números
    frase_limpa = "".join(caractere.lower() for caractere in entrada if caractere.isalnum())
    
    # Verifica se a frase limpa é igual a ela mesma invertida
    if frase_limpa == frase_limpa[::-1]:
        print(f'"{entrada}" é palíndromo\n')
    else:
        print(f'"{entrada}" não é palíndromo\n')