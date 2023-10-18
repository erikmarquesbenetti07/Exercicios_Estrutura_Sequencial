import math

# Solicita ao usuário que digite o raio do círculo
raio = float(input("Digite o raio do círculo: "))

# Calcula a área do círculo
area = math.pi * (raio ** 2)

# Exibe a área
print("A área do círculo com raio {:.2f} é {:.2f}".format(raio, area))
