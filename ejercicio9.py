# encoding: utf-8
import sys

peso = raw_input(" Ingrese su peso en Kg: ")
altura = raw_input(" Ingrese su altura en metros: ")

imc = round(float(peso) / float(float(altura) * float(altura)))
print "su IMC es de: "
print (imc)
