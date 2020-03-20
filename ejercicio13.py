# encoding: utf-8
import sys

inversion = float(input("Introduce la inversion inicial: "))
interes = 0.04
balance1 = inversion * (1 + interes)
print("Balance tras el primer ano:" + str(round(balance1, 2)))
balance2 = balance1 * (1 + interes)
print("Balance tras el segundo ano:" + str(round(balance2, 2)))
balance3 = balance2 * (1 + interes)
print("Balance tras el tercer ano:" + str(round(balance3, 2)))
