class Terrestre:
	def respirar(self):
		print('Respirar fuera del agua')
	def caminar(self):
		print('Estoy caminando')

class Acuatico:
	def respirar(self):
		print('Respiro bajo el agua')
	def nadar(self):
		print('Estoy nadando')

#Herenccia multiple 

class Anfibio(Acuatico, Terrestre):
	#Dependiendo del orden que coloquemos las clases de las que hereda,
	#dependerá cual método 'respirar' hereda.

	def saludar(self):
		print('Hola, soy un Anfibio.')


'''La primera que yo escogó aquí tiene ese nombre.
Cuando ponemos lo siguiente es algo reservado, if __name__ == '__main__':
significa que mi programa va a ejecutar sólo lo de este script, no lo de otros,
En este ejemplo no es tan visual, pero cuando jalamos clases de otro lado
es necesario para que no nos imprima lo del otro programa.
''' 

if __name__ == '__main__':
	#Creo un onjeto a partir de la clase anfibio: rana
	rana = Anfibio()
	#Con esto mando a ejecutar a rana, sus funciones
	
	rana.caminar()
	rana.nadar()
	rana.respirar()

	pez = Acuatico()
	pez.respirar()

'''
Notese que pez y rana realizan la acción respirar, sin embargo, 
en cada caso, el resultado es diferente a esta característica se le denomina polimorfismo,
el que el comportamiento de un método va a depender que objeto lo esté realizando. '''




