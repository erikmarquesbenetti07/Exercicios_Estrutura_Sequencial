# Solicita ao usuário que digite o valor da hora e o número de horas trabalhadas
valor_por_hora = float(input("Digite o valor que você ganha por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

# Calcula o salário bruto
salario_bruto = valor_por_hora * horas_trabalhadas

# Calcula os descontos
imposto_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

# Calcula o salário líquido
salario_liquido = salario_bruto - (imposto_renda + inss + sindicato)

# Exibe os resultados
print("+ Salário Bruto : R${:.2f}".format(salario_bruto))
print("- IR (11%) : R${:.2f}".format(imposto_renda))
print("- INSS (8%) : R${:.2f}".format(inss))
print("- Sindicato (5%) : R${:.2f}".format(sindicato))
print("= Salário Líquido : R${:.2f}".format(salario_liquido))
