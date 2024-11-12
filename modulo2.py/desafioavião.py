#um avião pode transportar até 1000kg. por cada mala transportada é cobrado um preço de 20$ 
#fazer um programa para ler o peso das malas a transportar sem ultrapassar o limite e indicar o valor apurado 

contar_malas=0
limite_peso=1000

while limite_peso>=0:
    peso_mala=float(input("introduza o peso da mala"))
    if peso_mala > limite_peso:
        break
    contar_malas=contar_malas + 1
    limite_peso=limite_peso - peso_mala
    print(f"ainda pode transportar mais{limite_peso}kg")
print(f"o valor a cobrar pelo transporte de malas é de {contar_malas*20}$")
