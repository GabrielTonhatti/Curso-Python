# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela
# a sua porção inteira.
# Ex:
# Digite um número: 6.127
# O número 6.127 tem a parte inteira 6.
print('Com a biblioteca math')
import math
num = float(input("Digite um número real qualquer: "))
print('O número {} tem a parte inteira {}'.format(num, math.trunc(num))) 
# "trunc" é pra pegar apenas a parte inteira do número

print('Com apenas o "trunc da bibilioteca math" importada')
from math import trunc
num = float(input("Digite um número real qualquer: "))
print('O número {} tem a parte inteira {}'.format(num, trunc(num))) 
# "trunc" é pra pegar apenas a parte inteira do número

print('Sem a biblioteca math')
num = float(input("Digite um número real qualquer: "))
print('O número {} tem a parte inteira {}'.format(num, int(num))) 
