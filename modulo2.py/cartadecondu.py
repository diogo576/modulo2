#algoritmo para 
pontos = 12 
opção = 0
infração_grave= 0
infração_leve= 0
infraçãom_grave = 0
while opção != 4:
    #mostrar pontos 
     print(pontos) 
    #mostrar as opções 
print("1.muito grave\n2,grave\n3,leve\n4,terminar")
    #ler a opção 
opção =input("1")
    #tirar os pontos 
if opção =="1":
    pontos = pontos - 6
    infraçãom_grave =infraçãom_grave + 1
if opção =="2":
     pontos = pontos - 4
     infração_grave =infração_grave + 1 
if opção == "3":
     if infração_leve >0:
            pontos = pontos -1 
     infração_leve = infração_leve + 1
if pontos < 0:
     pontos =0
#se tem uma infração m.grave ou 2 graves perde os pontos todos 
  

 