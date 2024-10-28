#programa para ler 10 numeros e indicar qual é o maior 

for i in range (10):
    numero = int(input("introduza o numero"))
    #se é o maior numero 
    if i == 0:
        maior = numero 
    else:
        if numero > maior :
        maior = 0 

print("o maior é",maior )
