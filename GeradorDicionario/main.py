minha_frase = input("Digite uma frase: ")

meu_dicionario = {}
for caracter in minha_frase:
    if caracter == " ":
        espaço = 1
    elif caracter not in meu_dicionario:
        meu_dicionario[caracter] = 1
    else:
        meu_dicionario[caracter] += 1

print (meu_dicionario)