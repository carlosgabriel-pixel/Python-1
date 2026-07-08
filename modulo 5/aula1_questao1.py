num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Calcula a diferença absoluta e arredonda para 2 casas decimais
diferenca = abs(num1 - num2)
resultado = round(diferenca, 2)

print(f"A diferença absoluta entre os números é: {resultado}")