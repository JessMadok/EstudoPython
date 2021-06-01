import math
tamanho_parede = float(input("Qual o tamanho em metros quadrados de sua parede? "))
litros_de_tintas = tamanho_parede/6
folga = math.ceil(litros_de_tintas * 0.1)
litros_de_tintas += folga
latas_18 = math.ceil(litros_de_tintas/18)
galoes_3 = math.ceil(litros_de_tintas/3.6)
custo_latas = latas_18 * 80
custo_galoes = galoes_3 * 25
print(f"{latas_18} latas de tinta ao custo de R${custo_latas}.")
print(f"{galoes_3} galoes de tinta ao custo de R${custo_galoes}.")



