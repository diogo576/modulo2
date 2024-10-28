# contar as vogais de uma frase 
frase= "ola mundo"

contar = 0
for letra in frase:
    if letra in "aeiou":
        contar = contar + 1 
print("a frase indicada tem",contar,"vogais")
     