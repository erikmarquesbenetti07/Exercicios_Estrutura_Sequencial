# Solicita ao usuário que digite a altura
altura = float(input("Digite a altura em metros: "))

# Calcula o peso ideal
peso_ideal = (72.7 * altura) - 58

# Exibe o peso ideal
print("O peso ideal para uma pessoa com altura", altura, "metros é de {:.2f} kg".format(peso_ideal))
