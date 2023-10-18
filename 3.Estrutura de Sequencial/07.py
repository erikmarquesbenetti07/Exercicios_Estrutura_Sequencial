# Solicita ao usuário que digite o lado do quadrado
lado = float(input("Digite o valor do lado do quadrado: "))

# Calcula a área do quadrado
area = lado ** 2

# Calcula o dobro da área
dobro_da_area = 2 * area

# Exibe o resultado
print("A área do quadrado é {:.2f}".format(area))
print("O dobro da área do quadrado é {:.2f}".format(dobro_da_area))
