# encoding: utf-8
import sys


nombre = raw_input("Como te llamas ")
if (nombre.islower()):
	print ("tiene" + str(len(nombre)) + "letras minusculas")
if (nombre.isupper()):
	print ("tiene" + str(len(nombre)) + "letras mayusculas")
	
#no se como identificar la letra mayuscula cuando ingrese el texto, pero creo que seria algo asi
