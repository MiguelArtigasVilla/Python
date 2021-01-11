miTupla=("Juan",13,1,1995)

print(miTupla[2])
#convertir tupla a lista
miLista=list(miTupla)
print(miLista)
print(miTupla)
#convertir lista a tupla
miLista2=["María",2,True,True]
miTupla2=tuple(miLista2)
print(miLista2[:])
print(miTupla2[:])
#numero de veces un elementos en tupla 
print(miTupla2.count(True)) 
#longitud de elementos
print(len(miTupla2))
#Tuplas unitarias 1 elemento
miTuplaUni=("Juan",)
print(len(miTuplaUni))
#empaquetado(desempaquetado) de tupla ( sin parantesis) para asignar a distintas variables
miTuplaSin="Juan",True,"2"
miTuplaCon=("María",False,3)
#desempaquetado
nombre,matrimonio,hijos =miTuplaCon
print (nombre)
print(hijos)
print(matrimonio)
a=1
b=True
c="Julio"
miTuplaEmpaquetada=a,b,c
print(miTuplaEmpaquetada[:])
X=miTupla2.count(True)
print(X)


