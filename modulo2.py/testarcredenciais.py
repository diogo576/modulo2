#ler email e palavra-pass
#se não forem corretos dar erro 
#permitir 3 tentativas
tentativas =3
while tentativas > 0:
    email=input("introduza o seu email")
    password=input("introduza a sua password")   
    if email=="juaquim@gmail.com" and password=="12345":
        print("login efetuado com sucesso ")
        break
    tetantivas =tentativas - 1 
    if email !="juaquim@gmail.com" and password != "12345":
        print("login falhou ") 
    elif email != "juaquim@gmail.com":
        print("email invalido")
    else:
        print("passwordf errada")
    if tentativas==0:
        print("atingiu o limite de tentativas,tente novamente mais tarde")
