# Solicita ao usuário que digite a temperatura em graus Fahrenheit
fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))

# Converte a temperatura para graus Celsius
celsius = 5 * ((fahrenheit - 32) / 9)

# Exibe o resultado
print("{:.2f} graus Fahrenheit é igual a {:.2f} graus Celsius".format(fahrenheit, celsius))
