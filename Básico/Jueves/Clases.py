######### Programación orienta a objetos ####### POO


#### POO : Orientación orientada a objetos #######

'''Es un paradigma de programación 
Todo lo que hagamos en python es un objeto, tiene propiedades y puede realizar acciones.
caracteristicas ---> atributos
acciones  ---->  metodos
 codeshare.io/pythonProteco


Clase: Es un molde para construir objetos
type nos regresa el tipo de dato 
'''

#Para crear la clase vamos a usar la palabra reservada class
####### METODO #####

#Self hace referencia a mi clase en si
#Self hace que no tengas que definir algunas características en todas las funciones
class Estudiante:
	#Metodo constructor: Método init : Se ejecuta automaticamente cuando yo instancio un método. Es con doble guión bajo 
	#Aquí esto instanciando cuando pongo armando=Estudiante("4526","GFAGG")
	def __init__(self, numero_cuenta, correo, nombre):
		#Para asignar las características a mi clase debo poner lo siguiente: 
        #Le doy las característica de mi estudiante
		#En la siguiente función pongo lo que hace la otra función
		self.numero_cuenta = numero_cuenta
		self.correo = correo
		self.nombre = nombre 
		print("Este es el método init")


	#def saludar(self, nombre): #Sino pongo self me mandará self
	def saludar(self): #Sino pongo self me mandará self
		print('Hola, ¿Cómo estás? .  Mi nombre es', self.nombre)
		#pass #Nos dice para saber que aquí voy a guardar una estructura, con esto no manda error


	def infomacion(self):
		print('Mi número de cuenta es: ', self.numero_cuenta)
		print("Mi número correo es: ", self.correo)
		print('Mi nombre es: ', self.nombre)
	

#es una variable que guarda un objeto, el objeto estudiante
#Cuando yo creo un objeto a partir de una clase, hago una instancia
#Aquí el orden si importa, no es tanto, pero pudo asignarle cual va con cual. Pero si cambio uno, debo de cambiar todos
#Sino va a mandar un error, es igual que en funciones
armando = Estudiante(nombre = "armando", numero_cuenta=2162626, correo="danielmpr.com")
julio = Estudiante("636234236","julio.com","julio")


print(armando.numero_cuenta, armando.correo) #Es un atributo, no lleva parentesís 
print(julio.numero_cuenta, julio.correo)


#Aquí lo estoy mandnado a llamar
armando.infomacion()
julio.infomacion()
armando.saludar()
julio.saludar()
#Comenté lo siguiente por que en la función saludar ya quite la variable nombre. 
#armando.saludar("armando") #Siempre debe llevar parentesis el método, aunque no lleve nada
#julio.saludar("julio")





















'''
init es el constructor, te dice las carácteristicas de los estudiantes
si defines otra función dentro del método, esa te dirá algo que pueda hacer el estudiante
CUIDAR CUANDO LO MANDAMOS A EJECUTAR
Para imprimir las caracterícas, sólo basta un print(ada, dadagt)
y para mandar a llamar la función es armando.NombreDeLaFuncion()
'''



#print(type(armando))
#print(type(2627.52))
#print(type('fafa'))

