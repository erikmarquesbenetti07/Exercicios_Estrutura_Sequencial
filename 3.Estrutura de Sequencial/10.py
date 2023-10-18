# Solicita ao usuário que digite a temperatura em graus Celsius
celsius = float(input("Digite a temperatura em graus Celsius: "))

# Converte a temperatura para graus Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Exibe o resultado
print("{:.2f} graus Celsius é igual a {:.2f} graus Fahrenheit".format(celsius, fahrenheit))
