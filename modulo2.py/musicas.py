#programa para calcular a duração de um album 

#ler número de musicas

n_musicas = int(input("quantas musicas deseja inserir "))
duração_total = 0
# ciclo para o n de musicas 
for i in range (n_musicas):

    #ler a duraçao
    musica = int(input("introduza a duração da musica em segundos")) 

    #validação
    while musica <= 0 or musica > 6000:
        print("a duração da musica nao é válida") 
    #somar a duração ao total 
    duração_total = musica + duração_total 

#converter a validação total para minutos:segundos
minutos = duração_total //60
segundos = duração_total % 60
#mostrar a duração total 
print(f"a duração do album é de {minutos}:{segundos}")
