# ler dois nomes e indicar qual deles o maior

nome1 = input("introduza o primeiro nome")
nome2 = input("introduza o segundo nome")

print(nome1,nome2)

t1 = len(nome1)
t2 = len(nome2)

if t1 > t2:
    print(f"o maior nome é {nome1}")
else:
    print(f"o maior nome é{nome2}")
