edad=int(input("ingresa la edad en años \n"))
if 0<=edad<=4:
    print("el cliente ingresa gratis")
if 4<=edad<=18:
    print("el cliente debe pagar 20000")
if 18<=edad<=60:
    print("el cliente debe pagar 15000")
if edad>60:
    print("el cliente solo paga el ingreso de 3000")

