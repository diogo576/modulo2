#programa para ler dois numeros e indicar se sao iguais ou diferentes 
#caso sejam diferentes indicar a diferença entre eles,com um valor positivo 
n1 = int(input("introduza um numero"))
n2 = int(input("introduza outro numero"))

if n1==n2:
    print("iguais")
else:
    print("diferentes")
    diferença=n1-n2
    if diferença<0:
        diferença= diferença*(-1)
    print("diferença")