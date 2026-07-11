import random

def encrypt(lista_nomes):
    # Gera uma chave aleatória entre 1 e 10
    chave = random.randint(1, 10)
    nomes_criptografados = []
    
    for nome in lista_nomes:
        nome_cripto = ""
        for caractere in nome:
            codigo_atual = ord(caractere)
            novo_codigo = codigo_atual + chave
            
            # Garante que o caractere se mantém no intervalo visível (33 a 126)
            if novo_codigo > 126:
                novo_codigo = 33 + (novo_codigo - 127) % 94
                
            nome_cripto += chr(novo_codigo)
        nomes_criptografados.append(nome_cripto)
        
    return nomes_criptografados, chave

# Teste com os dados do exemplo:
nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_cript, chave_gerada = encrypt(nomes)

print(f"chave_aleatoria = {chave_gerada}")
print(f"nomes_cript = {nomes_cript}")