#programa para ler um numero rel e listar os dez numeros de valor superior com incremento de 0.5 
#  no final apresentar a soma dos valores listados 
n= float(input("introdura um numero"))
adição= 0 
for i in range (10):
    n = n + 0.5 
    adição = n + adição 
print(adição)