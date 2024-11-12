x1=0
x2=1
numeros = int(input("introduz o limite da sequência"))
print(x1,"\numeros",x2)
for i in range (numeros - 2):
    soma = x1 + x2 
    print(soma)
    x1 = x2
    x2 = soma 

    
