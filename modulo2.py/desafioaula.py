

hora=int(input("hora"))

if hora>=5 and hora<=7:
    print("madrugada")
elif hora >=8 and hora <= 12:
    print("manhã")
elif hora >=13 and hora <=19:
    print("tarde")
else:
    print("noite")