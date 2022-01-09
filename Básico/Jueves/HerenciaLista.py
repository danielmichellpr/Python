#Vamos a agregar objetos a mi lista a través de objetos
class Milista(list):
	def append(self, objeto):
		print('Agregando un objeto a la lista')
		list.append(self,objeto)


lista = Milista((1,2,3,4,5))
lista.append(6)
print(lista)
lista1 = [1,4,5]
print(lista1)
lista1.append(8)
print(lista1)

