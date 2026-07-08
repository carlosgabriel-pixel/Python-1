# Fluxograma do cálculo de média e status do aluno
n1 = float(input())
n2 = float(input())
n3 = float(input())

m = (n1 + n2 + n3) / 3

if m >= 60:
    print("Aprovado")
elif m >= 40:
    print("Recuperação")
else:
    print("Reprovado")

print("fim")