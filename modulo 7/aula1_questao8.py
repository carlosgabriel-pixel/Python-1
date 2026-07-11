cpf_input = input("Digite seu CPF (XXX.XXX.XXX-XX): ")

# Remove pontos e traços, deixando apenas os números
cpf_limpo = cpf_input.replace(".", "").replace("-", "")

# Validação básica de tamanho
if len(cpf_limpo) != 11 or not cpf_limpo.isdigit():
    print("Inválido")
else:
    # --- CÁLCULO DO PRIMEIRO DÍGITO ---
    soma_1 = 0
    multiplicador_1 = 10
    for i in range(9):
        soma_1 += int(cpf_limpo[i]) * multiplicador_1
        multiplicador_1 -= 1
        
    resto_1 = soma_1 % 11
    digito_1 = 0 if resto_1 < 2 else 11 - resto_1

    # --- CÁLCULO DO SEGUNDO DÍGITO ---
    soma_2 = 0
    multiplicador_2 = 11
    # Desta vez incluímos os 9 primeiros dígitos + o primeiro dígito calculado
    for i in range(9):
        soma_2 += int(cpf_limpo[i]) * multiplicador_2
        multiplicador_2 -= 1
    soma_2 += digito_1 * 2  # Multiplicador do primeiro dígito validador é 2
        
    resto_2 = soma_2 % 11
    digito_2 = 0 if resto_2 < 2 else 11 - resto_2

    # --- VERIFICAÇÃO FINAL ---
    # Checa se os dígitos calculados batem com os digitados pelo usuário
    if int(cpf_limpo[9]) == digito_1 and int(cpf_limpo[10]) == digito_2:
        print("Válido")
    else:
        print("Inválido")