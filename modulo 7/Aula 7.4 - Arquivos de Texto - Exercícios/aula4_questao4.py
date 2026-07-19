import random

def carregar_enforcado():
    # Lê os blocos da arte ASCII do arquivo fornecido
    with open("gabarito_enforcado.txt", "r", encoding="utf-8") as f:
        conteudo = f.read()
    # Separa os estágios utilizando a marca de base da forca '=====' como divisor
    estagios = conteudo.strip().split("=====")
    # Reconstrói a base em cada item da lista para manter o desenho original
    return [estagio.strip() + "\n=====" for estagio in estagios if estagio.strip()]

def imprime_enforcado(erros, estagios_arte):
    print(estagios_arte[erros])

# Inicialização do Jogo
with open("gabarito_forca.txt", "r", encoding="utf-8") as f:
    palavras = [linha.strip().lower() for linha in f.readlines() if linha.strip()]

palavra_secreta = random.choice(palavras)
letras_descobertas = ["_" for _ in palavra_secreta]
estagios_arte = carregar_enforcado()

tentativas_restantes = 6
erros = 0
letras_tentadas = set()

print("*** BEM-VINDO AO JOGO DA FORCA ***")

while erros < 6 and "_" in letras_descobertas:
    print("\nPalavra: " + " ".join(letras_descobertas))
    print(f"Letras já tentadas: {', '.join(sorted(letras_tentadas))}")
    
    palpite = input("Digite uma letra para adivinhar: ").strip().lower()
    
    if not palpite or len(palpite) > 1 or not palpite.isalpha():
        print("Entrada inválida! Digite apenas uma letra.")
        continue
        
    if palpite in letras_tentadas:
        print("Você já tentou essa letra!")
        continue
        
    letras_tentadas.add(palpite)
    
    if palpite in palavra_secreta:
        print(f"Boa! A letra '{palpite}' está na palavra.")
        for idx, letra in enumerate(palavra_secreta):
            if letra == palpite:
                letras_descobertas[idx] = palpite
    else:
        print(f"Que pena, a letra '{palpite}' não está na palavra.")
        erros += 1
        imprime_enforcado(erros, estagios_arte)

# Finalização
if "_" not in letras_descobertas:
    print(f"\nParabéns! Você ganhou! A palavra era: {palavra_secreta.upper()}")
else:
    print(f"\nVocê foi enforcado! A palavra correta era: {palavra_secreta.upper()}")