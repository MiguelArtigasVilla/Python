
#1.imprimir "Hola Mundo"
print("Hola Mundo")

#2 variables numericas sumar y resultado
var1=4
var2=7
resultado=var1+var2
print("La suma de las variables es",resultado)

#3 IVA
valor=100.00
IVA=0.21
precioIVA=valor*IVA
precio=valor+precioIVA
print("El precio del IVA es",precioIVA,"$")
print("El precio con IVA es",precio,"$")

#4 Mayor de dos numeros
num1=5
num2=6
if num1>num2:
	print("El número mayor es",num1)
else:
	if num1==num2:
		print("Los números son iguales")
	else:
		print("El número mayor es",num2)

#5 variable entre 0 y 10
varnum=8
if 0<=varnum<=10:
	print("La variable numerica es",varnum," y está entre 0 y 10")
else:
	print("La variable numerica es ",varnum," y no esta entre 0 y 10")

#6 añador que si esta entre  11 y 20 muestre otro mensaje y si esta entre 21 y 30 eotro mensaje
varnum=28
if 0<=varnum<=10:
	print("La variable numerica es",varnum," y está  en el rango entre 0 y 10")
elif 11<=varnum<=20:
	print("La variable numerica es",varnum," y está en el rango entre 11 y 20")
elif 21<=varnum<=30:
	print("La variable numerica es",varnum," y está en el rango entre 21 y 30")
else:
	print("La variable numerica es ",varnum," y no esta en ningún rango de los indicados")

#7 numeros 1 a 100 while
contador=1
while contador<=100:
	print (contador)
	contador=contador+1

#8 7 pero con for
for i in range(100):
	i+=1
	print(i)

#9 caracteres hola mundo
for i in " !Hola Mundo! ":
	print (i)

#10  Mostrar pares entre 1 y 100
for i in range(50):
	print(2*(i+1))

#11 generar rango entre 0 y 10
rango_0_a_10=list(range(0,11))
print("Rango entre 0 y 10 : "+str(rango_0_a_10))

#12 Generar rango entre 5 y 10
rango_5_a_10=list(range(5,11))
print("Rango entre 5 y 10 : "+str(rango_5_a_10))


#13 Generar un rango entre 10 y 0
rango_10_a_0=list(range(10,-1,-1))
print("Rango entre 10 y 0 : "+str(rango_10_a_0))

#14 Generar un rango de 0 a 10 y de 15 a 20
rango_0_a_10=list(range(11))
rango_15_a_20=list(range(15,21))
rago_0_a_10_y_15_a_20= rango_0_a_10+rango_15_a_20
print("Rango de 0 a 10 y de 15 a 20 :"+str(rago_0_a_10_y_15_a_20))

#15 Generar un rango desde 0 hasta la longitud de la cadena "Hola mundo"
longitud_hola_mundo= len("Hola mundo")
rango_hola_mundo=list(range(longitud_hola_mundo+1))
print ("El rango es "+str(rango_hola_mundo))

#16 Pide dos cadenas por teclado, muestra ambas cadenas con un espacio entre ellas y con los dos promeros caracteres intercambiados
cadena_1=input("Introduzca la cadena 1 :")
cadena_2=input("Introduzca la cadena 2 :")
print("Cadena solicitada: "+cadena_2[:2]+cadena_1[2:]+" "+cadena_1[:2]+cadena_2[2:])

#17 Pide la cadena e indica si es un palidromo o no
cadena_3=input("Introduzca la cadena 3 :")
palindromo=cadena_3[::-1]
if cadena_3==palindromo:
	print(cadena_3+" es palindromo")
else:
	print(cadena_3+" no es palindromo")



#18 Adivina el numero entre 1 y 100
from secrets import *
def adivina():
	numero=randbelow(100)+1
	intentos=0
	prueba=input("Introduzca el primer intento: ")
	while int(prueba)!=numero:
		if int(prueba)<numero:
			print("El numero elegido es más alto que: "+prueba)
		else:
			print("El numero elegido es más bajo que: "+prueba)
		prueba=input("Introduzca el siguiente intento: ")
		intentos+=1
	print("!Enhorabuena¡ Has acertado en sólo "+str(intentos)+" intentos")
adivina()


#19 Funcion maximo
def maximo(n1,n2):
	if n1>n2:
		print (str(n1))
	elif n2>n1:
		print (str(n2))
	else:
		print ("Son iguales")

#20 Definir max_de_tres()

def max_de_tres(n1,n2,n3):
	if n1>n2 and n1>n3:
		print ("El numero mayor es: "+str(n1))
	elif n2>n1 and n2>n3:
		print ("El numero mayor es: "+str(n2))
	elif n3>n1 and n3>n2:
		print ("El numero mayor es: "+str(n3))
	elif n1==n2 and n1>n3:
		print ("Los numeros "+str(n1)+" y "+str(n2)+" son iguales y mayores que "+str(n3))
	elif n1==n3 and n1>n2:
		print ("Los numeros "+str(n1)+" y "+str(n3)+" son iguales y mayores que "+str(n2))
	elif n2==n3 and n2>n1:
		print ("Los numeros "+str(n2)+" y "+str(n3)+" son iguales y mayores que "+str(n1))
	else:
		print ("Los numeros "+str(n1)+" , "+str(m2)+" y "+str(n3)+" son iguales")

#21 Definir una funcion que calcule la longitud de una cadena o lista
def longitud_cadena(lista):
	print(str(len(lista)))

a=longitud_cadena("Esto es una prueba")


#22 Definir funcion que tome un caracter y devuevla True si es una vocal  de lo contrario devuelve false
def es_vocal(caracter):
	vocales=("a","e","i","o","u","A","E","I","O","U")
	if len(caracter)>1:
		print("Error hay mas de un carácter")
	elif caracter in vocales:
		print(True)
	else:
		print(False)	
ejemplo1="a"
ejemplo2="Z"
ejemplo3="ae"
es_vocal(ejemplo1)
es_vocal(ejemplo2)
es_vocal(ejemplo3)

#23 funcion sum y multip de listas
def sum(lista):
	resultado=0
	for i in lista:
		resultado+=int(i)
	return resultado	
	
a=[1,3,5,6,10]
print ("El resultado de la suma de los elementos de la lista es :"+str(sum(a)))

def multip(lista):
	resultado=1
	for i in lista:
		resultado*=int(i)
	return resultado

print ("El resultado del producto de los elementos de la lista es :"+str(multip(a)))

#24 Definir inversa 
def inversa(cadena):
	cadena_inversa=cadena[::-1]
	return cadena_inversa
cadena_prueba="estoy probando"
print("La cadena inversa de "+cadena_prueba+" es: "+inversa(cadena_prueba))

def inversa2(cadena):
	longitud=len(cadena)
	cadena_invertida=list(cadena)
	for i in cadena:
		cadena_invertida[longitud-1]=i
		longitud-=1
	return cadena_invertida

def inversa3(cadena):
	invertida=""
	indice=-1
	cont=len(cadena)
	indice=-1
	while cont >=1:
		invertida+=cadena[indice]
		indice-=1
		cont-=1
	return invertida

#25 funcion palindromo
def es_palindromo(cadena):
	if cadena==inversa(cadena):
		return True
	else:
		return False

cadena_prueba1="radar"
cadena_prueba2="Esta no es palindromo"
print(str(es_palindromo(cadena_prueba1)))
print(str(es_palindromo(cadena_prueba2)))

cadena4=inversa2("manolo")
print(cadena4)
cadena5=inversa3("el pescado")
print(cadena5)

#26 elemento superpuesto en listas
def superposicion(lista1,lista2):
	for i in lista1:
		for j in lista2:
			if i==j:
				return True
	return False
lista_1=["Madrid",9,False,7.23]
lista_2=["mADRID",3,True,8.23]
lista_3=["Malaga",3,True,8.23]

print (superposicion(lista_1,lista_3))
print (superposicion(lista_2,lista_3))

#27 generar caracteres
def generar_n_caracteres(numero, caracter):
	return caracter*int(numero)
print(generar_n_caracteres(7,"M"))	

#28 Histograma 
def procedimiento(lista):
	for i in lista:
		print (i*"*")
procedimiento([3,6,8,14,1])

#29	max y max_de_res
def max(num1,num2):
	if num1>num2:
		return num1
	else:
		return num2

def max_de_tres(num1,num2,num3):
	if num1>num2 and num1>num3:
		return num1
	elif num2>num1 and num2>num3:
		return num2
	else:
		return num3

def max_in_list(lista):
	maximo=lista[0]
	for i in lista:
		if i>maximo:
			maximo=i
	return maximo

print(max(4,6))
print(str(max_in_list([1,4,7,14,2,5,9])))

#30 def mas_larga()
def maslarga(lista):
	palabra_larga=""
	for i in lista:
		if len(i)>len(palabra_larga):
			palabra_larga=i
	return palabra_larga
lista_ejemplo=["casa","cadenas","mariposas","barco"]
print(maslarga(lista_ejemplo))

#31 filtrar palabtaras con mas de n caracteres
def filtrar_palabras(lista,longitud):
	palabras_mas_de_n=[]
	j=0
	for i in lista:
		if len(i)>longitud:
			palabras_mas_de_n.append(i)
			j+=1
	return palabras_mas_de_n	

listaejemplo=["mar","casa","ciudad","sol","banco","amanecer"]
print(filtrar_palabras(listaejemplo,4))

#32 pedir cadena a usuario yu contar cuantas mayusculas tiene
cadena_usuario=input("Introduzca la cadena para contar el número de mayúsculas: ")
contador=0
for i in cadena_usuario:
	if i!=i.lower():
		contador+=1
print("El número de mayusculas de la cadena "+cadena_usuario+" es "+str(contador))

#33 Programa convertir numeros binarios en enteros
numero_binario=input("Introduzca el número binario a convertir: ")
inverso=numero_binario[::-1]
suma=0
exponente=0
for  i in inverso:
	suma+=int(i)*2**exponente
	exponente+=1
print("El numero entero correspondiente a "+numero_binario+" es "+str(suma))

#34 Ingreso de añ. nombre y año de nacimiento de tres personas, calculo cuantos años cumplirarn  y se imprime
ano_en_curso=input("Por favor introduzca el año en curso: ")
print("El año introducido es: "+ano_en_curso)
for i in range (3):
	nombre=input("Introduzca el nombre de la persona: ")
	ano=input("Introduzca el año de nacimiento de la persona: ")
	print(nombre+" cumplirá "+str(int(ano_en_curso)-int(ano))+" años en "+ano_en_curso)	

#35 tupla 10 edades de personas

def mayores_20(tup):
	contador=0
	for i in tup:
		if i>20:
			contador+=1
	print("Hay "+str(contador)+" personas con edad superior a 20 años")
tupla_ejemplo=[4,27,15,44,35,112]
mayores_20(tupla_ejemplo)

#36metodo contar nombes que empiezan por un caracter

def contar_palabras_empiezan_n():
	contador=0
	lista=[]
	numero_nombres=input("Cuantos nombres quieres comparar: ")
	for i in range(int(numero_nombres)):
		lista.append(input("Cual es el siguiente nombre: "))

	caracter=input("Introduzca el carácter de comienzo: ")

	for i in lista:
		if i[0].lower()==caracter.lower():
			contador+=1
	print("El número de palabras que empiezan por "+caracter+" es "+str(contador))
contar_palabras_empiezan_n()

#37 contar vocales
def contar_vocales():
	diccionario_vocales={"a":0,"e":0,"i":0,"o":0,"u":0}
	lista_vocales=diccionario_vocales.keys()
	palabra=input("Intoduzca la palabra para contar las vocales: ")

	for i in palabra:
		for j in lista_vocales:
			if i==j :
				diccionario_vocales[j]+=1
	print (diccionario_vocales)
contar_vocales()

#38 es_bisiesto()
def es_bisiesto():
	ano=input("Introduzca el año a evaluar: ")
	if int(ano)%4==0 and int(ano)%100!=0:
		print("El año "+ano+" es bisiesto")
	else:
		print("El año "+ano+" no es bisiesto")

es_bisiesto()


