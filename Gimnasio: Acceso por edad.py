#Un gimnasio ofrece clases según la edad

edad = int(input("Dijite su edad: "))

if edad < 13:
    print("No debes ingresar")

elif edad >= 13 and edad <= 17:
    print("Clase juvenil")

elif edad >= 18 and edad <= 59:
    print("Clase general")

elif edad >= 60:
    print("clase senior")

    