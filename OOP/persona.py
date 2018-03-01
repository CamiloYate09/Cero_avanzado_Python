#PROGRAMACION ORIENTADA A OBJETO
from bz2 import __author__

#CLASES

__author__ = 'camiloY'

#SUPERCLASE


#CONSTRUCTOR
class Persona:
    def __init__(self,clave,nombre,edad):
        self.clave = clave
        self.nombre = nombre
        self.edad = edad
    
    def mostrarDatos(self):
        print("Mostrando datos desde la Super_clase")
        print("Clave:", self.clave)
        print("Nombre: ", self.nombre)
        print("Edad :", self.edad)