#definir una lista
lista=[]#esta listaesta vacia
lista2=[1,2,3,4]
print(lista2)
#acceder a umna posicion especifica a traves del index
print(lista2[2])
#ultimo elemento de la lista 
print(lista2[-1])
#penultimo elemento de una lista
print(lista2[-2])
#modificar un elemento de una posicion especifica
lista2[3]=15
print(lista2)
#recorrer la lista2 y multiplicarle por 2 sus elementos
for i in lista2:
    print(i*2)
#incluir el index en el recorrido,la iteracion
for index, i in enumerate(lista2):
    print(f"en la posicion {index} se encuentra el valor {i}")



numeros=[5,9,10]
generos=["jazz", "rock", "djent"]
#recorreer un ciclo las dos listas
for n,g in zip(numeros,generos):
    print(f"el numero {n} esta asociado con el genero {g} ")

print(len(generos))
generos.sort()
print(generos)
numeros.reverse()
print(numeros)
    
