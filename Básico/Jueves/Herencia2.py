
#Deben estar en la misma carpeta los dos archivos
#Con esto importo lo que está en el otro archivo

from Herencia import Animal
class Pato(Animal):
	def cuack(self):
		print('Cuack!!')

pato1=Pato()
pato1.cuack()
pato1.alimentarse()
pato1.respirar()