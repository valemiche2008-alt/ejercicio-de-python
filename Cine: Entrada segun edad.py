#el presio de la entrada cambia segun la edad 

edad = int(input("cuantos años tienes?: "))
 
if edad < 12:
    print("el costo de la entra es de 8.000")

elif edad >= 12 and edad <= 59:
    print("El costo de la entrada es de 12.000")

elif edad >= 60:
    print("el costo de su entrada es de 9.000")
    