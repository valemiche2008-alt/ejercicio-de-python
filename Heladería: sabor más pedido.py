#una heladeria quire registrar 5 pedidios por persona 

vainilla = 0
fresa = 0
chocolate = 0

# ciclo para registrar 5 veces 
for i in range(0,5,1):
    opciones = input("elige un sabor" "\n 1.Vainilla"+"\n 2.Fresa"+"\n 3.Chocolate"+"\n ingresa el sabor:")
    
    if (opciones == "1"):
        vainilla += 1
        print("Vainilla")
    
    elif (opciones == "2"):
        fresa += 1
        print("Fresa")

    elif (opciones == "3"):
        chocolate += 1
        print("Chocolate")
    
    else:
        print("opcion invalida, intenta de nuevo")

print(f"cantidad de vainilla {vainilla} cantidad de fresa {fresa} cantidad de chocolate {chocolate}")