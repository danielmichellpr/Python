class Perro:
    """
    Cuando anteponemos dos guiones bajo a un atributo o un
  pato.alimentarse()  método, Python le agrega al nombre de dicho atributo
    o método un guión bajo y el nombre de la clase
    """
    __patas = 4  #  -> _Perro__patas #Si ponemos dos guiones bajo 
    #a los atributos se vuelve un atributo privado. Se utiliza cuando no puedes modificar algo

    pelaje = True

    def __init__(self, Nom, Raza):
        self.nombre = Nom
        self.raza = Raza
        print('Se ha creado un nuevo perro')

    def __comer(self, alimento):  # -> _Perro__comer
        print('Soy %s y estoy comiendo %s' % (self.nombre, alimento))

    def ladrar(self):
        print('WOOOFF!!')


perro1 = Perro('Rufus', 'Dálmata')
perro1.ladrar()
#No se va a poder mandar a llamar __patas 
#print(perro1.__patas)
#Se tiene que mandar a llamar de la forma 
print(perro1._Perro__patas)

#Crear una caja de seguridad que sólo se abra cuando se le pasa la contraseña correcta
class CajaSeguridad():
    __contrasena = 1234
    def seguro(self,x):
        if x == self.__contrasena:
            print('La caja ha sido abierta')
        else:
            print('No se logró abrir')


caja =CajaSeguridad()
x=int(input("Introduce la clave: "))
caja.seguro(x)
