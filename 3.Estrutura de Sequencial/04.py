# Solicita ao usuário que digite as 4 notas bimestrais
nota1 = float(input("Digite a nota do 1º bimestre: "))
nota2 = float(input("Digite a nota do 2º bimestre: "))
nota3 = float(input("Digite a nota do 3º bimestre: "))
nota4 = float(input("Digite a nota do 4º bimestre: "))

# Calcula a média das notas
media = (nota1 + nota2 + nota3 + nota4) / 4

# Exibe a média
print("A média das notas é: {:.2f}".format(media))
