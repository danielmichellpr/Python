#### Herencia ####
#Es el hecho de que una clase pueda adquirir todos los mÃ©todos y atributos en otra
#Para que se herede a la nueva clase, se debe colocar el parentesis y dentro el nombre de la clase que se hereda


"""
Para crear una nueva clase debemos usar la palabra reservada class
seguido del nombre de la clase y dos puntos
"""


class Animal:
    """
    Los métodos de la clase se declaran al igual que las funciones, solo
    que estos deben encontrarse dentro del bloque de código de la clase
    y deben tener como primer parámetro 'self'
    """

    def alimentarse(self):  # Método alimentarse
        print('Me estoy alimentando!!')

    def respirar(self):  # Método crecer
        print('Estoy respirando!!!')


animal1 = Animal()  # Creamos dos instancias de la clase Animal
animal2 = Animal()  # Nombre de la clase seguido de dos parántesis
print(animal1.alimentarse())
  
