def datosFuncion():
	datos=[]
	nombre=input("Ingresa tu nombre: ")
	datos.append(nombre)
	apPat=input("Ingrese su apellido paterno: ")
	datos.append(apPat)
	numTel=int(input("Ingrese telefono: "))
	datos.append(numTel)
	numCue=int(input("Ingrese Numero Cuenta: "))
	datos.append(numCue)
	return datos
#datosFuncion()
#print(datosFuncion())
datosp1=datosFuncion()
datosp2=datosFuncion()
print(datosp1,datosp2)