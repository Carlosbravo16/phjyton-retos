baul=[]
seguir="s"
while seguir=="s" or seguir=="s":
    print("seleccione 1. agregar un elemento a la lista \n 2. listar articulos de baul \n 3. borrar ultimo elemento del baul \n 4. borrar articulo especifico del baul")
    de=int(input("que opcion deseas realizar"))
    if de==1:
        baul.append(input("ingrese el nombre de tu articulo"))
    elif de==2:
        print("estos son los articulos de tu baul \n")
        baul.sort( )
        print(baul)
    elif de==3:
        print(f"vas a eliminar el articulo", {baul[-1]})
        baul.pop()
        print(baul)

    elif de==4:
        for index,articulo in enumerate(baul):
            print(f"#{index} => {articulo}")
            baul.remove(int(input("ingrese el numero del articulo que desea borrar")))
            print("el baul quedo asi", baul)
    else:
        print("opcion incorrecta")
    seguir=input("deseas regresar al menu S/s o N para terminar ")