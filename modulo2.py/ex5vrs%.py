#ler as notas dos 10 alunos e caucular as percentagens de negativas e positivas 

n_alunos = 10 

soma = 0
for _ in range(n_alunos):
    nota = int(input("introduza uma nota"))
    soma =soma + nota 
#contar se a nota é positiva 
if nota>=10:
    contar_positiva = contar_positiva +1 

media = soma / n_alunos 
print(round(media,2))
print("nº de positivas",contar positivas)
print("nº de negativas",contar negativas)
# percentagens de positivas 
p_positivas = contar_positivas/ n_alunos * 100
print("a percentagens de positivas foi de",p_positivas)
print("a percentagem de negativas foi de",100-p_positivas)