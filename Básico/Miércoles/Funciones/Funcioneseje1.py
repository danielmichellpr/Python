import math
import os
'''
def soyUnaFuncion():
	#codigo que deamos que relice

soyUnaFuncion()#ejecucion de la funcion
'''

'''
def saludar():
	print("Hola! :D")
saludar()

def multiplicar(a,b,c):
	return a*b*c
print(multiplicar(2,3,4))
print(multiplicar(6,7,8))
print(multiplicar(9,1,0))
'''
def cuadrado(lado):
	return lado**2

def triangulo(base, altura):
	return (base*altura)/2

def circulo(radio):
	return math.pi*(radio**2)

while True:
	print("Calculadora de areas :D")
	opcion=int(input("Elige la opcion: \n1.- Cuadrado \n2.- Triangulo \n3.- Circulo \n4.- Salir\n"))
	os.system("cls")#os.system("clear")->Linux/Mac
	if(opcion==1):
		lado=float(input("Ingrese el lado: "))
		print(cuadrado(lado))
	elif(opcion==2):
		base=float(input("Ingrese la base: "))
		altura=float(input("Ingrese la altura: "))
		print(triangulo(base,altura))
	elif(opcion==3):
		radio=float(input("Dame el radio: "))
		print(circulo(radio))
	elif(opcion==4):
		break