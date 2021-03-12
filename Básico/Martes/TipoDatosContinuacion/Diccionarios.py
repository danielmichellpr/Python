'''
Tipos de datos basicos - Diccionarios
'''

diccionario={"a":"Armando",2:"Alejandro",3:"Julio"}
print(diccionario) #imprimimos todo el diccionario
print(diccionario["a"]) #accedemos por medio de la llave y nos retorna el valor
print(diccionario[2]) 
print(diccionario[3])
 
directorio={"Maria":54653298,"Juan":57575757,"Marla":54545454}

print("El telefono de Marla es: ",directorio["Marla"])
print("El telefono de Juan es: ",directorio["Juan"])
print("El telefono de Maria es: ",directorio["Maria"])

Paises=("Alemania","Mexico","Peru") #creamos una tupla
Capitales={Paises[0]:"Berlin",Paises[2]:"Lima",Paises[1]:"CDMX"} #asignamos como llave los valores de la tupla
print(Capitales) #imprimimos el diccionario Capitales


#Uso de metodos en diccionario
print(Capitales.keys()) #retorna las llaves
print(Capitales.values()) #retorna los valores
print(Capitales.items()) #retorna todos las llaves y valores en tuplas

print(len(Capitales)) #retorna la logitud  del diccionario Capitales
listae=[3,7,2,4,5,8,9,22,333,44,11,2,3]
print(len(listae)) # retorna la longitud de la listae