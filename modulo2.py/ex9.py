#um programa que le do utilizador um numero inteiro e indica se o numero é primo 

numero = int(input("introduza o numero a testar"))

primo= true

for i in range(2,numero):
    if numero % x ==0:
        primo= false

if primo == true:
    print("o nº",numero,"é primo")
else:
    print("o nº",numero,"nao é primo")

