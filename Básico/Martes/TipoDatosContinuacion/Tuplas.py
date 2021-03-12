'''
Tipos de datos basicos - Tuplas
'''

#COMENTARIO DE UNA LINEA

'''
Comentario
de 
varias 
lineas
'''
print(":D")

tup=() #tupla vacia
tup2 = (1, 2, 3, 4, 5 )
tup3 = ("a", "b", "c", "d")

Lista1=list(tup3) #casteo de una tupla a una tabla
print(Lista1) #imprimiendo la nueva lista
print(tup3) #imprimiendo la tupla original

lista=["a",1,"b",2]
print(lista)

tuplaNueva=tuple(lista) #Casteo de una lista a una tupla
print(tuplaNueva) #imprimiendo la tuplaNueva
print(lista) #imprimiendo la lista original

#tuplaNueva.append(2) #Arroja un error ya que las tuplas son inmutables

tup1 = ('hola', 'mundo', 1997, 2000)
print(tup1)

tup11 = 'hola', 'mundo', 1997, 2000 #empaquetado 
print(tup11)

informacionUs=("Julio", 7, 12, 1997)
nombre, dia, mes, año =informacionUs #desempaquetado
print(nombre)
print(dia)
print(mes)
print(año)

print(informacionUs[0]) #indexacion