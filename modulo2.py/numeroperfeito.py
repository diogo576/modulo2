#soma dos divisores é igual ao numero 
nº=int(input("introduza um numero"))
soma = 0
for i in range (1,nº):
    resto= nº % i
    if resto == 0 :
         soma = soma + i
if soma == nº :
    print("o numero é perfeito")
else:
    print("o numero nao e perfeito.a soma dos seus divisores foi ",soma)
