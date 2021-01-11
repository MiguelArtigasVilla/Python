#Crear diccionario
midiccionario={"Alemania":"Berlín","Francia":"París","Reino Unido":"Londres","España":"Madrid"}
#acceder a un elemento
print(midiccionario["Francia"])
#ver todos los elementos
print(midiccionario)
#añadir elementos
midiccionario["Italia"]="Lisboa"
print(midiccionario)
#asignar nuevo valor a clave existente se sobrescribe
midiccionario["Italia"]="Roma"
print(midiccionario)
#eliminar elemento
del midiccionario["Reino Unido"]
print(midiccionario)
#multiples tipos
midiccionariovariado={"Alemania":"Berlín",23:"Jordan","Mosqueteros":3}
print(midiccionariovariado)
#usar tupla para asignar valores
mitupla=("España","Francia","Reino Unido","Alemania")
midiccionario2={mitupla[0]:"Madrid",mitupla[1]:"París",mitupla[2]:"Londres",mitupla[3]:"Berlín"}
print(midiccionario2)
#añadir tupla en valores
midiccionario2={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","anillos":(1990,1992,1993,1996,1997,1998)}
print(midiccionario2)
print(midiccionario2["Equipo"])
print(midiccionario2["anillos"])
midiccionario3={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","anillos":{"temporadas":(1990,1992,1993,1996,1997,1998)}}
print(midiccionario3["anillos"])
#metod keys (claves), values (valores)
print(midiccionario3.keys())
print(midiccionario3.values())
print(len(midiccionario3))