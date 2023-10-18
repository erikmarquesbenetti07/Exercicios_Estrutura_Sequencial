# Solicita ao usuário que digite o tamanho da área a ser pintada em metros quadrados
area_a_ser_pintada = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

# Define a cobertura da tinta (1 litro para cada 6 metros quadrados)
cobertura_por_litro = 6

# Define o tamanho das latas de tinta (18 litros), o preço da lata e o tamanho dos galões (3,6 litros), e o preço do galão
litros_por_lata = 18
preco_por_lata = 80.00
litros_por_galao = 3.6
preco_por_galao = 25.00

# Calcula a quantidade de litros de tinta necessários
litros_necessarios = (area_a_ser_pintada * 1.1) / cobertura_por_litro  # 10% de folga

# Calcula a quantidade de latas de tinta necessárias
latas_necessarias = litros_necessarios / litros_por_lata

# Arredonda para cima para garantir que você compre latas suficientes
import math
latas_necessarias = math.ceil(latas_necessarias)

# Calcula o preço total ao comprar apenas latas de 18 litros
preco_total_latas = latas_necessarias * preco_por_lata

# Calcula a quantidade de galões de tinta necessários
galoes_necessarios = litros_necessarios / litros_por_galao

# Arredonda para cima para garantir que você compre galões suficientes
galoes_necessarios = math.ceil(galoes_necessarios)

# Calcula o preço total ao comprar apenas galões de 3,6 litros
preco_total_galoes = galoes_necessarios * preco_por_galao

# Calcula a quantidade de latas e galões necessários para minimizar o desperdício
latas_minimas = int(litros_necessarios / litros_por_lata)
litros_restantes = litros_necessarios - (latas_minimas * litros_por_lata)
galoes_minimos = math.ceil(litros_restantes / litros_por_galao)

# Calcula o preço total ao misturar latas e galões
preco_total_misturado = (latas_minimas * preco_por_lata) + (galoes_minimos * preco_por_galao)

# Exibe os resultados
print("Quantidade de latas de 18 litros a serem compradas:", latas_necessarias)
print("Preço total ao comprar apenas latas de 18 litros: R${:.2f}".format(preco_total_latas))
print("Quantidade de galões de 3,6 litros a serem comprados:", galoes_necessarios)
print("Preço total ao comprar apenas galões de 3,6 litros: R${:.2f}".format(preco_total_galoes))
print("Quantidade mínima de latas de 18 litros:", latas_minimas)
print("Quantidade mínima de galões de 3,6 litros:", galoes_minimos)
print("Preço total ao misturar latas e galões: R${:.2f}".format(preco_total_misturado))
