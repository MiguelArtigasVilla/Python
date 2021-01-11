miLista=["María","Pepe","Marta","Antonio"]

print (miLista[:])

print(miLista[0])
print(miLista[-2])
print(miLista[:2])
print(miLista[1:])
#Añade al final
miLista.append("Sandra")
print(miLista[:])
#Añade en la posicion
miLista.insert(3,"Guillermo")
print(miLista[:])
#Añade varios elementos
miLista.extend(["Juan","Alicia","Ana"])
print(miLista[:])
#devuelve indice de un elemento
print(miLista.index("Ana"))
miLista.append("Pepe")
#si hay varias ocurrecias devuelve el primero
print(miLista.index("Pepe"))
#Para saber si existe un elemento
print("Sandra" in miLista)
print("Miguel" in miLista)
#admite varios tipos
listaVariada=[2,True,"calor",3.75]
print (listaVariada[:])
#Eliminar elemento
listaVariada.remove("calor")
print(listaVariada[:])
#eliminar elemento en ultima posicion 
listaVariada.pop()
print(listaVariada[:])
#sumar listas diferentes
miLista=["María",5, True,78.35]
miLista2=["Sandra","Lucia"]
miLista3=miLista+miLista2
print(miLista3[:])
#repetirlista
miLista5=["María",4,True]*4
print(miLista5[:])
