#somar os numeros pares de 1 a 100

numero_1=int(input("introduza um numero"))
soma = 0
for i in range (2,101,2):
    soma = soma + i
print(soma)
