nomes = ["André", "Murilo", "José", "Jessica", "Melissa", "Juliana"]
meu_nome = input("Digite o nome que voce quer procurar: ").title()

for nome in nomes:
    if nome == meu_nome:
        busca = True
        break
    else:
        busca = False

if busca == True:
    print("ACHOU!")
else:
    print("O nome procurado nao consta na lista")
