#pedir la hora de llegada de clientes en un formato

hora = int(input("coloque le numero de la hora de llegada: "))

if hora >= 6 and hora <= 11:
    print("Llego en las horas de la mañana")

elif hora >= 12 and hora <= 17:
    print("Llego en las horas de la tarde")

elif hora >= 18 and hora <=22:
    print("Llego en las horas de la tarde")

else:
    print("Fuera de la hora laboral")
    