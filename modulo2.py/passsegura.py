#programa para dizer se a palavrapasse é segura ou não
# tem de ter letras 
#tem de ter pelo menos uma maiuscula e uma minuscula 
#tem de ter numeros
#tem de ter pelo menos 8 caracteres
#tem de ter um caracter especial:!?@$.,;:-_

a_M="ABCDEFGHIJKLMNOPQSTUVXWYZ"
a_m=a_M.lower()
A_numeros="0123456789"
A_simbolos="!:.@!"
tem_M =False 
tem_min= False 
tem_s=False 
tem_n=False
passe=input("introduza a palavar passe a testar ")
for letra in a_M:
    if letra in passe:
        tem_M==True 
        break
for letra in a_m:
    if letra in passe:
        tem_min= True 
        break 
for letra in A_numeros:
    if letra in passe:
        tem_n= True 
        break
for letra in A_simbolos:
    if letra in passe:
        tem_s= True
        break
if tem_M==True and tem_min==True and tem_n== True and tem_s==True:
    print("palavra passe segura")
else:
    print("palavra passe não é segura")



    
