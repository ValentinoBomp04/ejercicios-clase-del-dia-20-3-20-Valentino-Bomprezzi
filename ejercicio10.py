# encoding: utf-8
import sys

dividendo= raw_input("Introduce el dividendo (entero): ")
divisor = raw_input("Introduce el divisor (entero): ")
print(dividendo + " entre " +  divisor + " da un cociente " + str(int(dividendo) // int(divisor)) + " y un resto " + str(int(dividendo) % int(divisor)))
