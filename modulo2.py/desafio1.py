#programa para determinar a que classe pertence um jogador 
#pedir ao utilizador a idade do jogador 
idade= int(input("introduza a idade do jogador"))
#dizer a que escalão pertence o jogador 
#se a idade do jogador for menor que 10(infantis)
if idade < 10:
    print("o jogador pertence a casse de infantis")
#se idade do jogador for menor ou igual 10 e menor que 14(iniiciados)
if idade >=10 and idade < 14:
#se idade do jogador 
    print("o jogador pertence a clase de iniciados")
if idade >=14 and idade < 18:
    print("o jogador pertence a clase de juniores")
if idade >= 18:
    print("o jogador pertence a classe de seniores")
