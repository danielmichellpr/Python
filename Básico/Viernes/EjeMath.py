#Las importaciones generalmente van hasta arriba 
#Aunque se pueden ir declarando después, pero no se podrán 
#usar antes 
import math



#dir para elistar todo lo que contiene el módulo
#print(dir(math))

x = math.sin(2)
# \t me va dar un tabulador
print('\t El seno de 2 es:',x )

#Puedo mandar a llamarlo como se llama mi función 
#Aunque es palabra reservada, necesita su paquetería
sin = "No tengo nada, pero me llamo como una función trigonométrica. "
print(sin)

#Puedo importar un paquetería y ponerle un apodo
import math as m
# Con esta otra manera mandamos a importar todo
# from math import *
y = m.radians(180)
j = m.degrees(m.pi)
print('\n\n\t El valor de', 180, 'grados en radianes es: ', y)
print('\n\n\t El valor de', m.pi, 'radianes en grados es: ', j)

from random import *

#\n enter
#\t tabulador 

z = randint(-2,2)
i = randint(-2,2)
print('\n\n\t El número aleatorio entre -2 y 2 es: ', z)
print('\n\n\t El número aleatorio entre -2 y 2 es: ', i)


#from time import sleep
import time
print("\n\n\t Voy a poner atención")
sleep(2) #Nos da un delay para la siguiente parte
print("\n\n\t No me dormí, estaba parpadenado lento")

#$###

#a = m.radians(180)
#b = m.degrees(m.pi)
print('\n\t El valor del coseno de 1 sobre pi es: ', math.cos((1/math.pi)))
print('\n\t El valor del seno de pi medio es: ', math.sin((math.pi/2)))


'''area de un circulo de radio 2 
1.- De manera manual creando tus variables
2.- importar el módulo math, y utilizar la entidad pi '''
r=2
pi = 3.13159
print('\n\t El área de un circulo de radio dos es: ', pi*(r**2))
print('\n\t El área de un circulo de radio dos es: ', math.pi*(r**2))

#Puedo mandar a llamar sólo algunos métodos, poniéndole coma
