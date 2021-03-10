'''
Tipos de datos basicos - Listas
'''

#Son estructuras de datos dinamicas de alto nivel que representan una
#coleccion ordenada de objetos

enteros = [1,2,3,22,5,6,7,8,9] #lista de enteros
print(enteros)

copiaenteros=enteros[:] #haciendo un slicing regresa una lista nueva
print(copiaenteros) #imprimiendo copiaenteros
print(enteros[4:]) #lista con slicing desde el elemento 4 al final
print(enteros) #no se afecta la lista original

vocales = ["o","e","i","a","u"]
print(vocales)
print(vocales[3:]) #lista con slicing desde el elemento 3 al final
print(vocales[3]) #Manda a imprimir solo el elemento que se encuentra en ese indice 

#Metodos en las listas
enteros.append(4) #agrega el objeto al final de la lista
enteros.sort() #ordena la lista en orden ascendente

enteros2 = [8,7,6,5,4,3,2,1,0]

enteros.extend(enteros2) #Anexa la lista enteros2 a la lista enteros1
enteros.insert(0, 30) #inserta un 30 en el indice 0
enteros.insert(7, 60) #Inserta un 60 en el indice 7
enteros.insert(12,60) #Inserta un 60 en el indice 12
enteros.remove(60) #quita el objeto especificado de lista
            #importante recordar, no quita el objeto que este en el indice 60, sino el primer 60 como tal que encuentre
enteros.pop(0) #elimina el ultimo elemento
#enteros.clear() #limpia toda la lista
print(enteros.count(1)) #cuenta cuantas veces aparece en la lista el elemento especificado
print(enteros)
enteros.reverse() #ordena la lista en forma descendente
print(enteros)
print(enteros.copy()) #entrega una copia de la lista
print(vocales.copy()) #entrega una copia de la lista
print(enteros.index(1))#nos regresa el indice de la pirmera ocurencia que encontro

b = [2,5,"hola",7,"Mundo"] #pueden tener tipos de datos mezclados