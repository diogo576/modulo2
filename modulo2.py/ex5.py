#ler as notas de 10 alunos e caucula a media 

soma = 0
for i in range(10):
    nota=int(input("introduza uma nota"))
    soma= soma + nota 

media = soma/10
  
print(media)
