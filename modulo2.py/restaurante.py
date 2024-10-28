#programa para ler as entradas de clientes para cada mesa 

mesas = 10
lugares = mesas * 5

for mesas_ocupadas in range(mesas):
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


    