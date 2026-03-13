#registra 5 personas en un gimnasio

name =input("cual es su nombre?:")

day =int(input("cuantos dia asistio a la semana?:"))

min =int(input("cuantos minutos a entrenado por dia?:"))

if day < 3:
    print("tiene bajo compromiso")

elif day >= 3 and day <= 4:
    print("tiene medio compromiso")

elif day >= 5:
    print("tiene comprimiso alto")

