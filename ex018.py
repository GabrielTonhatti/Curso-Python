# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse ângulo.
import math
ang = float(input('Digite o ângulo que você deseja: \n'))
seno = math.sin(math.radians(ang))
cosse = math.cos(math.radians(ang))
tange = math.tan(math.radians(ang))

print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, seno))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang, cosse))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(ang, tange))

print()
print('Importanto apenas o "sin(seno), cos(cosseno), tan(tangente) e radians(radianos)"')
from math import sin, cos, tan, radians
ang = float(input('Digite o ângulo que você deseja: \n'))
seno = sin(radians(ang))
cosse = cos(radians(ang))
tange = tan(radians(ang))

print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, seno))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang, cosse))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(ang, tange))
