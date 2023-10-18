# Solicita ao usuário que digite a altura em metros
altura = float(input("Digite a altura em metros: "))

# Solicita ao usuário que informe o sexo (M para masculino, F para feminino)
sexo = input("Informe o sexo (M para masculino, F para feminino): ")

if sexo == "M" or sexo == "m":
    # Calcula o peso ideal para homens
    peso_ideal = (72.7 * altura) - 58
    print("O peso ideal para um homem com altura", altura, "metros é de {:.2f} kg".format(peso_ideal))
elif sexo == "F" or sexo == "f":
    # Calcula o peso ideal para mulheres
    peso_ideal = (62.1 * altura) - 44.7
    print("O peso ideal para uma mulher com altura", altura, "metros é de {:.2f} kg".format(peso_ideal))
else:
    print("Sexo não reconhecido. Use M para masculino ou F para feminino.")
