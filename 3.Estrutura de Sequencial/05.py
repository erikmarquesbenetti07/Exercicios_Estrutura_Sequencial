# Solicita ao usuário que digite a medida em metros
metros = float(input("Digite a medida em metros: "))

# Converte metros para centímetros
centimetros = metros * 100

# Exibe o resultado da conversão
print("{:.2f} metros é igual a {:.2f} centímetros".format(metros, centimetros))
