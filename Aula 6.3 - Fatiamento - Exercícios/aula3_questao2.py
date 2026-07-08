urls = [
    "www.google.com", 
    "www.gmail.com", 
    "www.github.com", 
    "www.reddit.com", 
    "www.yahoo.com"
]

dominios = []

# Como todas começam com "www." (4 caracteres) e terminam com ".com" (4 caracteres)
# Utilizamos o fatiamento [4:-4] para pegar apenas o conteúdo do meio
for url in urls:
    nome_principal = url[4:-4]
    dominios.append(nome_principal)

print(f"URLs: {urls}")
print(f"dominios: {dominios}")