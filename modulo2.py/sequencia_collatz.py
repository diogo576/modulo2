#peir ao utilizador um numero inteiro positivo e escrever a sequencia de collatz ate chegar em 1.
nº= int(input("introduza um numero"))
contar = 0
while nº != 1:
    resto=nº % 2
    if resto == 0:
        nº = nº // 2
    else:
        nº =nº * 3 + 1 
    print("nº")
