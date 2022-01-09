class Estudiante:
	'''
	Esta es una clase estudiante
	Las comillas así se imprimirán a la hora 
	de mandar a llamar la ayuda y nos servirá para documentar
	'''
	def __init__(self,nombre,carrera,serie):
		self.nombre = nombre
		self.carrera = carrera
		#No es necesario ponerla con la misma que en el __init__ 
		self.seriefav = serie
	
	def VerSerie(self):
		print("Estoy viendo mi serie favorita, es:", self.seriefav)
	
	def TomarCafe(self):
		print("Estoy nervioso por tomar café")

	def Estudiar(self, lenguaje_favorito, idioma= "inglés"):
		print("Estoy estudiando:", lenguaje_favorito, "y también aprendo", idioma)

	def Informacion(self):
		print("Soy", self.nombre, "y estoy estudiando la carrera de:", self.carrera)

Daniel = Estudiante("Daniel","Física","TBBT")

Daniel.Informacion()
Daniel.VerSerie()
Daniel.TomarCafe()
Daniel.Estudiar("Python")


#La función help nos ayuda a tener información de lo que buscamos

print(help(Estudiante))