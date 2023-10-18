# Solicita ao usuário que digite o peso de peixes em quilos
peso = float(input("Digite o peso de peixes (em quilos): "))

# Define o limite de peso estabelecido pelo regulamento (50 quilos)
limite = 50.0

# Verifica se o peso excede o limite
if peso > limite:
    excesso = peso - limite
    multa = excesso * 4.0  # R$4,00 por quilo excedente
    print("Peso excedente: {:.2f} quilos".format(excesso))
    print("Multa a ser paga: R${:.2f}".format(multa))
else:
    excesso = 0
    multa = 0
    print("Peso dentro do limite, não há multa a ser paga.")

