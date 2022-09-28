#acomulador debe iniciar en 0 antes del ciclo
total=0
#contador debe iniciar en 0 antes del ciclo
minutos=0
for i in range(0,3,1):
    precio=int(input("ingrese el precio del producto"))
    cantidad=int(input("ingrese la cantidad de producto"))
    subtotal=precio*cantidad
    #acomulador viven dentro de un ciclo
    #aumentan en un valor variable
    total=total+subtotal
    print(f"el costo del desayunito es {total}")
    #contador vive dentro de un  
    #aumenta en un valor fijo
    minutos=minutos+1
    #minutos+=1 
print(f"por esta compra obtuviste{minutos} minutos para recargar a tu movil exito")
print("adios")
