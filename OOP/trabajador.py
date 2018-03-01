'''
Created on 1 mar. 2018

@author: Kernel-2018
'''

from OOP.persona import Persona # IMPORTANTO CLASE

class Trabajador(Persona):#DE QUE CLASE VAMOS A HEREDAR TODO
    def  __init__(self,clave,nombre,edad,sueldo):
        self.clave = clave
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo
    def mostrarDatos(self):
        print("Mostrando datos desde la Sub_clase")
        print("Clave:", self.clave)
        print("Nombre: ", self.nombre)
        print("Edad :", self.edad)
        print("Sueldo:", self.sueldo)



