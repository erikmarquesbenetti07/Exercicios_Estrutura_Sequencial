# Solicita ao usuário que digite o valor da hora e o número de horas trabalhadas
valor_por_hora = float(input("Digite o valor que você ganha por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

# Calcula o salário total
salario_total = valor_por_hora * horas_trabalhadas

# Exibe o resultado
print("Seu salário total no mês é R${:.2f}".format(salario_total))
