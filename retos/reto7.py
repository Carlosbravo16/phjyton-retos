from random import randint
saldo=0
repeat="si"
repetir="si"
juego=0
while repeat=="si" or repeat=="si":
    plata=int(input(" ingrese el saldo que desea recargar "))
    saldo=saldo+plata 
    print("su saldo global es de ",saldo)
    if saldo>=0:
        repeat=input(f"si desea ingresar mas dinero escriba si de lo contrario escriba no \n" )
    else:
        break
apuesta=int(input("ingrese el valor que desea apostar\n"))
while repetir=="si" or repetir=="si":
    moneda=randint(1,2)
    eleccion=int(input("digite 1 para escoger cara y 2 para escoger sello "))
    if moneda==1 and eleccion==1:
        saldo=saldo+apuesta
        juego=juego+1
        print(" salio cara, usted escogio cara ganaste!,  debes duplicar tu apuesta")
    elif moneda==1 and eleccion==2:
        saldo=saldo+apuesta
        juego=juego+1
        print("salio cara, usted escogio sello perdiste!")
    elif moneda==2 and eleccion==2:
        saldo=saldo-apuesta
        juego=juego+1
        print("salio sello, usted escogio sello ganaste!, debes duplicar tu apuest")
    elif moneda==2 and eleccion==1:
        saldo=saldo-apuesta
        juego=juego+1
        print("salio sello, usted escogio cara perdiste!")
    elif eleccion!=1 or eleccion!=2:
        print("digitaste una opcion incorrecta")
    else:
        print("datos incorrectos")
    print(f"su saldo actual es ",saldo)
    repetir=input(f"quiere jugar de nuevo escriba si o de lo contrario escriba no \n")
    if repetir=="si" or repetir=="si":
        apuesta=int(input("ingrese el valor que desee apostar \n"))
    else:
        break
    print("el numero de veces que usted jugo fue ",juego," el dinero acumulado fue ",saldo)
