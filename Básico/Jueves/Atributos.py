class circulo:
	#pi es una variable de clase y radio de una instancia
	pi=3.14159

	def __init__(self, radio):
		self.radio = radio

#Puedo poner directo el pi porque pertecene a la clase, no al objeto
print(circulo.pi)

#Lo tengo que definir para cada uno por ser atributo de instancia
circuloA= circulo(10)
print(circuloA.radio)
circuloB = circulo(50)
print(circuloB.radio)



class Triangulo:
	#Método Estático: Hago uso de la función sin necesidad de crear el objeto
	#Si ponemos staticmethod no es necesario el self y nos mandará error yviceversa
	@staticmethod
	#Ya no necesito self porque ya no voy a usar instancia
	def area(base, altura):
		return(base*altura)/2

MiTriangulo = Triangulo()
print(MiTriangulo.area(10,20))

#Así sólo reproduzco sin llamar a la instancia
resultado = Triangulo.area(10,20)
print(resultado)
resultado = Triangulo.area(100,200)
print(resultado)
resultado = Triangulo.area(300,500)
print(resultado)


