# Lista contendo tuplas com informações dos 10 livros
livros = [
    ("O Caçador de Pipas", "Khaled Hosseini", "2003", "368"),
    ("Torto Arado", "Itamar Vieira Junior", "2019", "264"),
    ("Dom Casmurro", "Machado de Assis", "1899", "256"),
    ("1984", "George Orwell", "1949", "336"),
    ("O Pequeno Príncipe", "Antoine de Saint-Exupéry", "1943", "96"),
    ("O Hobbit", "J.R.R. Tolkien", "1937", "328"),
    ("A Garota no Trem", "Paula Hawkins", "2015", "378"),
    ("Sapiens", "Yuval Noah Harari", "2011", "464"),
    ("Fahrenheit 451", "Ray Bradbury", "1953", "216"),
    ("Duna", "Frank Herbert", "1965", "680")
]

with open("meus_livros.csv", "w", encoding="utf-8") as f:
    # Escreve o cabeçalho original
    f.write("Título,Autor,Ano de publicação,Número de páginas\n")
    
    # Escreve os registros de cada livro
    for titulo, autor, ano, paginas in livros:
        f.write(f"{titulo},{autor},{ano},{paginas}\n")

print("Arquivo 'meus_livros.csv' gerado com sucesso!")