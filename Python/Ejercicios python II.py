#Ejercicio 1 Examen de Inteligencia de Negocios 2020-06-19
def asignaturas():
	notas={}
	suspensas=[]
	while True:
		asignatura=input("Introduce una asignatura ")
		calificacion=input("Introduce la nota ")
		notas[asignatura]=calificacion
		if float(calificacion)<5.0:
			suspensas.append(asignatura)
			break

	print("Las asignaturas suspensas son: ")
	print(asignatura)

asignaturas()