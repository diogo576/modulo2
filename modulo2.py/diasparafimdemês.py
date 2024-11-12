#programa para ler um ano mes e dia e dizer qunantos dias falta para acabar o mês

ano=int(input("introduz o ano "))
mês= int(input("introduz o mês "))
dia= int(input("introduz o dia "))

dia_mes=31
if mês == 4 or mês == 6 or mês == 9 or mês == 11:
    dias_mes= 30
    
elif mês == 2:
    if (ano % 4 == 0 and ano % 100 != 0 )or ano % 400==0:
        dias_mes=29
    else:
        dias_mes= 28 
faltam= dias_mes - dia 
print("faltam",faltam,"dias para o fim do mês")
