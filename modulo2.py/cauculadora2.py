escolha = "s"
while escolha == "s":
    n1 = int(input("introduza o primeiro numero"))
    n2 = int(input("introduza o segundo numero"))
    #pedir ao utilizador qual cauculo quer executar 
    operação = input("introduz a operação, soma subtração divisão multiplicação")
    resultado = 0
    if operação == "soma":
        resultado = n1 + n2 
    elif operação == "subtração":
        resultado = n1 - n2
    elif operação == "divisão":
        resultado = n1 / n2 
    elif operação == "multiplicação":
        resultado = n1 * n2
    else:
        print("operação não é valida")
        #definir a variável resultado com nada 
        resultado = None 

    if resultado is not None:
        print(resultado)

#perguntar se pretende continuar 
escolha = input("pretende continuar a fazer contas(s/n)")
escolha = escolha.strip().lower()