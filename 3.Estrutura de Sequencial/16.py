# Solicita ao usuário que digite o tamanho da área a ser pintada em metros quadrados
area_a_ser_pintada = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

# Define a cobertura da tinta (1 litro para cada 3 metros quadrados)
cobertura_por_litro = 3

# Define o tamanho da lata de tinta (18 litros) e o preço da lata
litros_por_lata = 18
preco_por_lata = 80.00

# Calcula a quantidade de litros de tinta necessários
litros_necessarios = area_a_ser_pintada / cobertura_por_litro

# Calcula a quantidade de latas de tinta necessárias
latas_necessarias = litros_necessarios / litros_por_lata

# Arredonda para cima para garantir que você compre latas suficientes
import math
latas_necessarias = math.ceil(latas_necessarias)

# Calcula o preço total
preco_total = latas_necessarias * preco_por_lata

# Exibe os resultados
print("Quantidade de latas de tinta a serem compradas:", latas_necessarias)
print("Preço total: R${:.2f}".format(preco_total))
