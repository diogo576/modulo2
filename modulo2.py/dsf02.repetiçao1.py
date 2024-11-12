#programa para ler os tempos á passagem na meta e no fim de 5 voltas mostrar o tempo total dispendido(soma dos tempos 
# de cada volta 
#ler cada tempo de passagem na meta 
voltas=5 
total=0
#mostrar o tempo total dispendido(soma dos tempos)
for i in range(5):
    minutos=int(input("introduz os minutos de cada volta"))
    total = (minutos * voltas) 
print(total)