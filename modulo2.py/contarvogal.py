#ler 10 letras e antes de terminar o programa indicar quantas vogais o utilizador introduziu

contar_vogais = 0 
for i in range(10):
    letra = input("introduza uma letra")
    letra = letra.strip #remover os espacos em branco no inicio e no final da string 
    if len(letra) != 1:
        print("so pode inserir uma letra")
    else:
        if letra in "aeiouAEIOU":
            contar_vogais  = contar_vogais + 1
print(contar_vogais)