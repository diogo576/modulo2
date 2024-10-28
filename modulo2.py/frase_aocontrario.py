#ler uma frase do utilizador e mostrar uma letra por linha por ordem inversa 

frase =input("introduza uma frase")
#ciclo para percorrer a frase letra a letra mas por ordem invertida 
for posição in range(len(frase)-1,-1,-1):
    print(frase(posição))
