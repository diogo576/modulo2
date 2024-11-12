#programa para ler as notas de uma turma e indicar o nº do aluno com melhor nota 
#deve começarpor ler o nº de alunos 
melhor_nota=-1
numero_aluno=-1
nº_alunos=int(input("introduza o nº de alunos "))
for i in range(nº_alunos):
    nota=int(input(f"nota do aluno nº{i + 1}"))
    if nota > melhor_nota:
        melhor_nota=nota 
        numero_aluno=i + 1
print("o aluno com melhor nota é o nº,{numero_aluno}$")