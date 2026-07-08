# Resolvendo o problema das cobaias do laboratorio
N = int(input())

total_coelhos = 0
total_ratos = 0
total_sapos = 0

for _ in range(N):
    entrada = input().split()
    quantia = int(entrada[0])
    tipo = entrada[1]
    
    if tipo == 'C':
        total_coelhos += quantia
    elif tipo == 'R':
        total_ratos += quantia
    elif tipo == 'S':
        total_sapos += quantia

total_cobaias = total_coelhos + total_ratos + total_sapos

# Calculando as porcentagens
p_coelhos = (total_coelhos / total_cobaias) * 100
p_ratos = (total_ratos / total_cobaias) * 100
p_sapos = (total_sapos / total_cobaias) * 100

# Exibindo os resultados no formato exato do exemplo
print(f"Total: {total_cobaias} cobaias")
print(f"Total de coelhos: {total_coelhos}")
print(f"Total de ratos: {total_ratos}")
print(f"Total de sapos: {total_sapos}")
print(f"Percentual de coelhos: {p_coelhos:.2f} %")
print(f"Percentual de ratos: {p_ratos:.2f} %")
print(f"Percentual de sapos: {p_sapos:.2f} %")