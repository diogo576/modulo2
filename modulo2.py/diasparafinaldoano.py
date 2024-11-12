dia= int(input("introduz o dia")) 
ano=int(input("introduz o ano "))
mes_atual= int(input("introduz o mês "))
soma = 0

for i in range(mes_atual,3):
    dia_mes = 31
    if mes_atual == 4 or mes_atual == 6 or mes_atual == 9 or mes_atual == 11:
        dias_mes= 30
        
    elif mes_atual == 2:
        if (ano % 4 == 0 and ano % 100 != 0 )or ano % 400==0:
            dias_mes=29
        else:
            dias_mes= 28 
faltam =dia_mes - dia 
soma = soma + faltam 
print("faltam",soma,"dias para o fim do ano")

