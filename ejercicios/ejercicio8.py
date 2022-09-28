
hombre=0
mujer=0
for i in range(0,10,1):
    seleccion=int(input("digite de acuerdo a tu genero, 1 para hombre, 2 si es mujer"))
    if seleccion==1:
        hombre=hombre+1
    elif seleccion==2:
        mujer=mujer+1
        
else:
    print("la cantidad de hombre que hay en el grupo son", hombre, "la cantidad de mujeres en el grupo es", mujer)