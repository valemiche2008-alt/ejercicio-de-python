# en una cafeteria venden y cuestan

cafe = 4000
te = 3500
jugo = 5000

# cuales bebidas quiere y cuantas 

bebida = input("¿Que bebida deseas? (1. cafe, 2. te, 3. jugo):")

varios = int(input("cuantas quieres?: "))

if bebida == "1":
    total = cafe * varios

elif bebida == "2":
    total = te * varios

elif bebida == "3":
    total = jugo * varios

else:
    print("bebida no encontrada")
    
print("Total a pagar es de: ", total)