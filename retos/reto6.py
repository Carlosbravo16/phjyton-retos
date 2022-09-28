from random import randint
eleccion=int(input("oprima 1 para ingrese el valor de su factura o oprima 2 para ingresar la cantidad de productos comprados \n"))
if eleccion==1:
    compra=int(input("ingrese el valor de su compra\n"))
else:
    numproductos=int(input("ingrese el numero de productos a comprar "))
    valorproducto=10000
    compra=numproductos*valorproducto

descuento=randint(1,4)
total=compra 
if compra>50000:
    print("salio escogido para participar en nuestro sorteo de aniversario")
    if descuento==1:
        calculodesc=compra*0.10
        total=compra-calculodesc
        print("salio balota roja, su descuento es del 10% en el valor de su factura, su total a pagar es" , total)
    elif descuento==2:
        calculodesc=compra*0.30
        total=compra-calculodesc
        print("salio balota azul, su descuento es del 30% en el valor de su factura, su total a pagar es" , total)
    elif descuento==3:
        calculodesc=compra*0.50
        total=compra-calculodesc
        print("salio balota amarilla, su descuento es del 50% en el valor de su factura, su total a pagar es" , total)
    elif descuento==4:
        print("salio balota blanca, te llevas totalmente gratis tu compra")
    else:
        print(f"el sorteo escogio{descuento}")
else:
    print("no fue escogido para participar en nuestra promocion, su total a pagar es ", compra)
if descuento==1 or descuento==2 or descuento==3:
    valorrecibido=int(input("ingrese el valor con el que desea cancelar"))
    cambio=valorrecibido-total
    print("su compra fue ",total," producto se realizo el pago con ",valorrecibido," su cambio es ",cambio)
else:
    descuento==4
    print("ganaste")

    

    
