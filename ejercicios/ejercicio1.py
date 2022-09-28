numproductos=int(input("ingrese el numero de productos a comprar "))
valorproducto=10000
factura=numproductos*valorproducto
print ("la cantidad que usted compro fueron ",numproductos," productos el valor total a pagar es ",factura)
valorrecibido=int(input("ingrese el valor con el que desea cancelar "))
cambio=valorrecibido-factura
print ("su compra fue de ",numproductos," productos que realizo el pago con ",valorrecibido," su cambio es ",cambio)
