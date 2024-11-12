#pedir ao ultilizador os tres lados do triangulo
a= int(input("introduza um valor"))
b=int(input("introduza outro valor"))
c=int(input("introduza o ultimo valor"))
if a>0 and b>0 and c>0:
    if (a+b)>c or (b+c)>a or (a+c)>b:
        print("triangulo válido")
    if a == b and b == c:
        print("equilatero")
    elif a == b or a == c or b == c:
        print("isosceles")
    # se não 
    else:
        print("escaleno")
