
caminho1= (input("Zoro se perdeu novamente, ajude-o a encontrar seu bando novamente. Em seu primeiro caminho para onde ele deve seguir?(direita/esquerda): ")).lower()
if caminho1 == "esquerda":
    caminho2 = (input("Zoro seguiu na direção correta. Mas agora ele deve passar pelo lago ou pela caverna? (lago/caverna): ")).lower()
    if caminho2 == "lago":
        caminho3 = (input("Zoro atravessou o lago sem maiores problemas e está cada vez mais perto do seu bando, agora uma montanha está na sua frente, para subi-la o que ele deve escolher? (escada/corda): ")).lower()
        if caminho3 == "corda":
            caminho4 = (input("Ufa Zoro já está vendo o navio dos chapeus de palha, mas ele deve através as portas do castelo.(azul/vermelha/amarela): ")).lower()
            if caminho4 == "amarela":
                print("Parabéns, Zoro finalmente encontrou seu bando")
            else:
                print("Infelizmente Zoro se perdeu de vez.")
        else:
            print("Infelizmente Zoro se perdeu de vez.")
    else:
        print("Infelizmente Zoro se perdeu de vez.")
else:
    print("Infelizmente Zoro se perdeu de vez.")
