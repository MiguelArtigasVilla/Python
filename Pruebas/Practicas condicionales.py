'''salario_presidente=int(input("Introduce salario presidente "))
print("Salario presidente: "+str(salario_presidente))

salario_director=int(input("Introduce salario director "))
print("Salario director: "+str(salario_director))

salario_jefe_area=int(input("Introduce salario Jefe Área "))
print("Salario Jefe Área: "+str(salario_jefe_area))

salario_administrativo=int(input("Introduce salario Administrativo "))
print("Salario administrativo: "+str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
	print("Todo funciona correctamente")
else:
	print("Algo falla en esta empresa")


print("Programa de becas")
distancia_escuela=int(input("Introduce la distancia a la escuela en Km "))
print(distancia_escuela)
numero_hermanos=int(input("Introduce el número de hermanos en el centro "))
print(numero_hermanos)
salario_familiar=int(input("Introduce el salario anual bruto "))
if distancia_escuela>40 and numero_hermanos>2 and salario_familiar<=20000:
	print("Tienes derecho a beca")
else:
	print("No tienes derecho a beca")
'''
print("Asignaturas optativas Año 2021")
print("Asignaturas optativas: Informática gráfica - Pruebas de software - Usabilidad y accesibilidad")
opcion=input("Escribe la asignatura escogida: ")
asignatura=opcion.lower()
if asignatura in ("informática gráfica", "pruebas de software", "usabilidad y accesibilidad") :
	print("Asignatura elegida " + asignatura)
else:
	print("La asignatura escogida no está contemplada")