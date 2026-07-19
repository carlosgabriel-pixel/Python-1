import csv

musicas_por_ano = {}

with open("spotify-2023.csv", "r", encoding="latin-1") as f:
    # O csv.reader lida nativamente com as aspas no arquivo de dados
    leitor = csv.reader(f)
    cabecalho = next(leitor)
    
    # Índices com base nas colunas exigidas pelo enunciado
    idx_name = cabecalho.index("track_name")
    idx_artist = cabecalho.index("artist(s)_name")
    idx_year = cabecalho.index("released_year")
    idx_streams = cabecalho.index("streams")
    
    for linha in leitor:
        try:
            # Filtro de regras do enunciado: Ignorar músicas contendo aspas internas explícitas nos nomes
            if '"' in linha[idx_name] or '"' in linha[idx_artist]:
                continue
                
            ano = int(linha[idx_year])
            
            # Restringe o intervalo entre os anos de 2012 e 2022
            if 2012 <= ano <= 2022:
                # Converte os streams para inteiro para comparação numérica correta
                streams = int(linha[idx_streams])
                
                info_musica = [linha[idx_name], linha[idx_artist], ano, streams]
                
                # Se for o primeiro registro do ano ou tiver mais streams que o recorde anterior
                if ano not in musicas_por_ano or streams > musicas_por_ano[ano][3]:
                    musicas_por_ano[ano] = info_musica
                    
        except ValueError:
            # Ignora linhas com dados corrompidos ou incompletos nos campos numéricos
            continue

# Monta e ordena a lista final em ordem cronológica de anos (2012 a 2022)
lista_final = [musicas_por_ano[ano] for ano in sorted(musicas_por_ano.keys())]

# Exibe o resultado final estruturado
print("[")
for elemento in lista_final:
    print(f"  {elemento},")
print("]")