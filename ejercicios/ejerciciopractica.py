presupuesto=100000
gasto1=0

while presupuesto>=0 and presupuesto<=100000:
    gasto=int(input("ingrese el valor de gasto \n"))
    presupuesto=presupuesto-gasto
    gasto1=gasto1+1
    print(f"el gasto fue, {gasto} su saldo es {presupuesto}")
    if gasto1 <=2:
        print("puede seguir con su compra")
    else:
        break
print(f"sin fondos")
