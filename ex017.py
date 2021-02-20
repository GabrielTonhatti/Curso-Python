# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
# triângulo retângulo, calcule e mostra o comprimento da hipotenusa

catetoO = float(input('Qual o comprimento do cateto oposto? \n'))
catetoA = float(input('Qual o comprimento do cateto adjacente? \n'))
hipot = (catetoO ** 2 + catetoA ** 2) ** (1/2)

print('A hipotenusa vai medir {:.2f}!'.format(hipot))

print()
print('Importanto toda a biblioteca math')
import math
catetoO = float(input('Qual o comprimento do cateto oposto? \n'))
catetoA = float(input('Qual o comprimento do cateto adjacente? \n'))
hipot = math.hypot(catetoO, catetoA)

print('A hipotenusa vai medir {:.2f}!'.format(hipot))

print()
print('Importanto apenas a hipotenusa da biblioteca math')
from math import hypot
catetoO = float(input('Qual o comprimento do cateto oposto? \n'))
catetoA = float(input('Qual o comprimento do cateto adjacente? \n'))
hipot = hypot(catetoO, catetoA)

print('A hipotenusa vai medir {:.2f}!'.format(hipot))