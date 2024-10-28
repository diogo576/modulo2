#programa para indicar quanto dinheiro podemos gastar e quanto podemos carregar de peso 

#ler orcamento e o peso do utilizador
orçamento = float(input ("quanto dinheiro tem para as compras"))
peso = float(input("quanto peso pode carregar"))
#enquanto tiver orçamento e o peso
while orçamento > 0 and peso > 0: 
    #ler o preço e o peso do produto comprado 
    preço = float(input("indique o preço do produto comprado "))
    
    #se o preço é zero terminar o ciclo 
    if preço == 0:
        break
    peso_produto = float(input("indique o peso do produto comprado"))
    #nao posso ultrapassar o orçamento nem o peso 
    if orçamento < preço or peso < peso_produto:
        print("nao tem dinheiro suficiente")
    else:
    #atualizar o orçamento e o peso 
        orçamento = orçamento - preço 
        peso = peso - peso_produto 
    #mostrar o orçamento e o peso restante 
    print(f"ainda tem {orçamento} e ainda tem {peso}kg")

print("acabou as suas compras")