# encoding: utf-8
import sys

inversion = float(raw_input("Cantidad a invertir "))
interes = float(raw_input("Interés porcentual anual "))
anos = int(input("Anos"))
print("Capital final: " + str(round(inversion * (interes / 100 + 1) ** anos, 2)))
