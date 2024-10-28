#surtear um numero entre 1 e 10 
import random

#sortear o nº
numero_secreto = random.randint (1,10)

#pedir ao utillizador um nº
t1 = int(input("intoduza um nº de 1 a 10: "))

#testar e informar se é maior,igual ou menor 
if numero_secreto == t1:
    print("acertou")
else:
    if t1> numero_secreto:
        print("o nº secreto é menor")
    else:
        print("o nº secreto é maior")

    #pedir ao utillizador um nº
    t1 = int(input("intoduza um nº de 1 a 10: "))

    #testar e informar se é maior,igual ou menor 
    if numero_secreto == t1:
        print("acertou")
    else:
        if t1> numero_secreto:
            print("o nº secreto é menor")
        else:
            print("o nº secreto é maior")

            #pedir ao utillizador um nº
        t1 = int(input("intoduza um nº de 1 a 10: "))

        #testar e informar se é maior,igual ou menor 
        if numero_secreto == t1:
            print("acertou")
        else: 
            print (f"o numero secreto é: {numero_secreto}")