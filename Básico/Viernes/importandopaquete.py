import paquete

#Nos va a regresar las descripciones de los __init__
#help(paquete)

#Con esto importe el script que se encuentra en la carpeta de
#paquete llamada promedios
import paquete.promedios

#Aquí seleccionó una función de promedios llamada promedios_titulo
#Inserto sus parámetros y me realiza la función.
paquete.promedios.promedio_titulo("MuestreoA",1,6,842,742,42,52,5)



import paquete.NumerosPrimos.funciones as funciones
# help(funciones) : Nos mostrará lo que tiene el script de funciones y sus comentarios

print(paquete.NumerosPrimos.funciones.lista_primos(30))
funciones.lista_primos(30)