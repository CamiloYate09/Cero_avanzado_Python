'''
Created on 1 mar. 2018

@author: Kernel-2018
'''
from OOP.trabajador import *


#CREANDO INSTANCIAS (OBJETOS)

personita = Persona("s55s5", "Diana Morales", 15)

trabajadorcito = Trabajador("s4s45s5", "Tatiana Morales",  23, 1250000)

#DEJANDO VER DATOS

personita.mostrarDatos()
print()
trabajadorcito.mostrarDatos()
