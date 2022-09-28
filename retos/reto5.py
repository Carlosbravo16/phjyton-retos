from random import randint


compra=int(input("ingresa el valor de compra \n"))
descuento=randint(1,4)
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
    print("lastimosamente tu compra no aplica para participar en nuestro sorteo de aniversario, valor de factura" ,compra)
    
