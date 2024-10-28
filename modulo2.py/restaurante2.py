#programa para ler a entrada de clientes para cada mesas 

mesas = 10
lugares = mesas * 5

while mesas > 0:
     n_clientes = int(input("quantas pessoas para entrar:"))
       if n_clientes>lugares:
        print("nao tem lugares para tantos clientes")
        break
    #ocupar uma mesa
    mesas = mesas - 1
    #ocupar os lugares 
    lugares = lugares - n_clientes
    print("mesas ocupadas:",mesas_ocupadas)
    print("lugares disponiveis:",lugares)

print("o restaurante está cheio")