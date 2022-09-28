from random import randint


yo=randint(1,3)
maquina=randint(1,3)
eleccion=int(input("digite 1 para escoger piedra, 2 para escoger papel y 3 para escoger tijera "))

if yo==1 and maquina==2 :
    print("escogi piedra, la maquina papel, pierdo!...")
elif yo==1 and maquina==3 :
    print("ecogi piedra, la maquina tijera, gano!...")
elif yo==2 and maquina==3 :
    print("escogi papel, la maquina tijera, pierdo!...")
elif yo==2 and maquina==1 :
    print("escogi papel, la maquina piedra, gano!...")
elif yo==3 and maquina==1 :
    print("escogi tijera, la maquina piedra, pierdo!...")
elif yo==3 and maquina==2 :
    print("escogi tijera, la maquina papel, gano!... ")
else:
    print("ambos saca lo mismo hay un empate")

