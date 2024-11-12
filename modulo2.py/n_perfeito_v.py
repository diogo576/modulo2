numero= int(input("introduza um numero"))

for k in range (1,numero):
    soma = 0
    for i in range(1,k):
        resto=k % i
        if resto== 0:
            soma = soma + i
    if soma == k:
        print(f"nº{k}é perfeito")
    else:
        print(f"nº{k}não é perfeito. a soma dos seus divisores é de",soma )
        