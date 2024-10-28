"""
programa para somar todos os valores inteiros entre x e y 
o utilizador é que indica os valores para y e para x
"""
x = int(input("introduza o primeiro valor a somar"))
y =int(input("introduza o segundo valor a somar "))

soma = 0

if x < y:
    incremento= 1
else :
    incremento = -1

for i in range(x,y+incremento,incremento):
    soma= soma + i

print(soma)