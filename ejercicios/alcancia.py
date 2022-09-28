repetir="s"
alcancia=0

while repetir=="S" or repetir=="s":
    plata=int(input("ingrese el valor a ahorrar"))
    alcancia=alcancia+plata
    repetir=input("desea ingresar mas dinero s o n para salir")
    print(f"el total ahorrado es {alcancia}")
    if alcancia<=200000:
        print("puedes seguir ahorrando")
    else:
        print(f"el total del ahorro es {alcancia} no puedes seguir ingrsando mas dinero")
        break
print(f"llegaste al tope de ahorro") 

