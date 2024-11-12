#programa para depositar dinheiro 
#ver saldo 
saldo=0
escolha=0

#depositar dinheiro (0.01-10000)
while escolha!=4:
    print("atm\n1.ver saldo\n2.depositar\n3.levantar\n4.terminar")
    escolha=int(input())
    if escolha== 1 :
        print("ver saldo")
    if escolha== 2:
        valor=float(input("valor a depositar"))
        #testar nº de casas decimais 
        d=valor - round(valor,2)
    if valor < 0.01 or valor > 10000:
         print("o valor introduzido nao é valido")
    else:
        saldo=saldo + valor 
        print("o seu saldo atualmente é de",saldo)
if escolha == 3:
    valor=float(input("qual o valor a levantar"))
    if valor < 10 or valor > 400 or valor> saldo:
        print("valor indicado nao é valido")
    else:
        saldo = saldo - valor 
        print("o seu saldo atualmente é de",saldo)
