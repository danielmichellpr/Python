"""
Clase de control de flujo para el curso intersemestral de python 2020-1

For
	For-each
	Con rangos
Listas por comprensión
"""

"""
Ciclo for

La sentencia for permite iterar a través de
los elementos de cualquier secuencia ordenada
o objeto iterable (iterar -> repetir) y
ejecutar un bloque de códigos por cada una.
El elemento de cada ciclo se almacena en una
variable que se encuentra después de la
palabra reservada for.

Entre los objetos sobre los que se puede
iterar se encuentra:

● listas
● tuplas
● diccionarios
● cadenas de texto
● ‘range’
● archivos
"""

########## For-each ##########

# Iteración sobre una lista
numeros = [1, 2,3 ,4 ,5, 6, 7, 8,9, 10]
for numero in numeros:
	print(numero)


print("\n****************************************************")

# Iteración sobre una tupla
tup = ("hola",1,2,4,4)
for miembro in tup:
    print(miembro)



print("\n****************************************************")


# Podemos iterar sobre una Tupla que tenga otras tuplas o listas
valores = ( (35, 25), ["Hola", "Mundo"], (True, False) )
# Imprimir cada valor de la tupla
for valor in valores:
	print(valor)


print("\n****************************************************")

# Si cada objeto dentro de la tupla tiene dos valores y queremos obtener esos valores lo hacemos de la siguiente manera
for valor1, valor2 in valores:
	print(valor1, valor2)


print("\n****************************************************")
	
# Para obtener tres valores:
valores = ( (10, 20, 30), ["Hola", "Mundo", "Python"], (True, False, True) )
for valor1, valor2, valor3 in valores:
	print(valor1, valor2, valor3)


print("\n****************************************************")


# Iteraciones sobre diccionarios	(Sólo me da las llaves)
diccionario = {'clave a':1, 'clave b':2}
for llave in diccionario:
	print(llave)



print("\n****************************************************")



dic = {"Titular": "Julio","Adjunto": "Armando","Auxiliar": "Montecillo"}
# Podemos obtener los valores a partir de las llaves
for instructor in dic.keys():
    print(instructor,dic[instructor])



#No se puede obtener las keys a partir de los valores
for nombre_intructor in dic.values():
	print(nombre_intructor)

# Iteración sobre una letra
for letter in "esternocleidomastoideo":
    print(letter, end = "")

print("\n ****************************************************")

##### Ejercicio ####
"""
Mostrar los pares del 1 al 10 y mostrar los impares multiplicados por 5 utilzando for
"""

for numero in [1, 2, 3, 4, 5, 6, 7,8 ,9, 10]:
	if numero%2 == 0:
		print("El número es par y es: ", numero)
	else:
		print("El número es impar y multiplcado por 5 es:", 5*numero)

print("\n****************************************************")
############################ Con rangos ############

# Con la función range podemos generar números para iterar sobre estos

# For que se repite 10 veces
# range(10) genera 10 números
for numero in range(10):
	print(numero)

# Definir un rango
# range(número de inicio, número final-1)
for numero in range(5, 10):
	print(numero)


for numero in range(1, 11):
	if numero %2 :
		print(numero*5)
	else:
		print(numero)

# Es posibel definir rango con número negativos
for numero in range(-10, 11):
	print(numero)

# Definir saltos
# range(inicio, final-1, saltos)
for numero in range(1, 101, 2):
	print(numero)


# Si el número a iterar no es importante colocamos un guión bajo

print("\n****************************************************")
cantidad = 0
print(cantidad)
for _ in range(10):
	cantidad+=10
print(cantidad)


print("\n****************************************************")

# Combinar range con len
lista = [1, 2, 3, 4, 5, 6]
for indice in range(len(lista)):
	print("Indice: ", indice, " valor: ", lista[indice])


print("\n****************************************************")

# enumerate nos devuelve el índice y el valor que se encuentra en ese índice
for indice, valor in enumerate(lista):
	print("Indice: ", indice, " valor: ", valor)

print("\n")
print("\n")
######################### Break y continue ###########################

mensaje = "Esta es una string larga posible de iterar"

# La palabra break rome el ciclo, todo lo demás ya no se ejecuta
for caracter in mensaje:
	if caracter == "i":
		break
	print(caracter,end="")


print("\n****************************************************")




# Continue salta una iteración
# Cuando caracter == "P" no se ejecuta lo demás y salta a la siguiente iteración
for caracter in mensaje:
	if caracter == "i":
		continue
	print(caracter, end="")

print("\n****************************************************")

lista = [1, 2, 3,4 ,5, 6, 7, 8, 9, 10]

for numero in lista:
	if numero==5:
		continue
	print(numero, end="")

print("\n****************************************************")
################## Matrices ################
filas = 5 ##filas,
columnas = 5 ##columnas
sublista = []
lista = []
for i in range(filas):
    for j in range(columnas):
        sublista.append(0)				#En cada iteración crea una sublista, que está en el ciclo de j
    lista.append(sublista)				#Cuando pasa todos los "j" para un cierto "i", eso lo guarda en lista
    sublista = []						#reinicia la sublista y se repite el proceso

print(lista)

for i in range(filas):
    for j in range(columnas):
        print(lista[i][j],end = "")
    print("")


###################### Ejercicio ##################
"""
Hacer el Fizz-buzz
Recorrer los números de 1 al 100
Si el número es divisible por 3 imprimir Fizz
Si el número es divisible por 5 imprimir Buzz
Si el número es divisible por 3 y 5 imprimir Fizz Buzz
Si el número no es divisible ni por 3 ni por 5 imprimir el número
"""


"""
for numero in range(1,101):
	if numero%3==0 and numero%5==0:
		print("Fizz Buzz")
	elif numero%3==0:
		print("Fizz")
	elif numero%5==0:
		print("Buzz")
	else:
		print(numero)

"""

for numero in range(1,101):
	valor=""
	if numero%3==0:
		valor="Fizz"
	if numero%5==0:
		valor+="Buzz"
	if numero%3 != 0 and numero %5 != 0:
		valor=numero
	print(valor)

###################### Ejercicio 2 ###################

# Mostrar en pantalla la frecuencia de aparición de vocales en una frase dada por el usuario.

frase="Hola Mundo"
frase=frase.lower()
vocales = {}
for letra in frase:
	if letra in ["a", "e", "i", "o", "u"]:
		vocales[letra] = frase.count(letra)

print(vocales)


#################### Listas por comprensión ##########3

print("\n********************************************")

lista=[]
for _ in range(10):
	lista.append(0)

lista = [0 for valor in range(10)]
print(lista)

# Crear una lista con sólo números pares
lista2 = [valor for valor in range(10) if valor%2==0]
print(lista2)

listita = [[1,2,3],[4,5,6],[7,8,9]]
lista7 = [ numero for lista in listita for numero in lista]
print(lista7)

print("Tuplas con listas")
##Podemos crear tuplas
##puntos(x,y) donde y sea el cuadrado de x
tam = 5
lista9 = [(x,x**2) for x in range(tam)]
print(lista9)

# Podemos crear tuplas más complejas
lista10 = [(x,y) for x in range(3) for y in range(2)]
print(lista10)

print("Tuplas")
estructura = tuple( (x for x in range(0, 101) if x%2 == 0 if x<50) )
print(estructura)

print("Diccionarios")
diccionario = {indice: valor for indice, valor in enumerate(lista)}
print(diccionario)

calificaciones = [("Julio",8),("Amando",9),("Montecillo",8)]

reportes = {tupla[0] : tupla[1] for tupla in calificaciones}
print(reportes)

# Si tu nombre lleva una a tienes un punto extra
nombres = list(reportes.keys())
for nombre in nombres:
	if "a" in nombre.lower():
		reportes[nombre] += 1

print(reportes)

# Diccionarios anidados
Partidos = [["Pumas vs America",1,0],["Atlas vs Necaxa",1,2],["Chivas vs Crus Azul",2,3]]

resultados = { partido[0]:{ 'marcador':[partido[1],partido[2]]} for partido in Partidos}
print(resultados)

print(resultados.get("Atlas vs Necaxa").get('marcador'))