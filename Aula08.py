#Importar biblioteca Math(Matemática)
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz do número {} é igual a {:.2f}'.format(num, raiz))

print()
print('Aredondar pra cima!')
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz do número {} é igual a {:.2f}'.format(num, math.ceil(raiz)))

print()
print('Aredondar pra baixo!')
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz do número {} é igual a {:.2f}'.format(num, math.floor(raiz)))

print()
# importar apenas o sqrt(calcular a raiz quadrada)
print('Calcular a raiz quadrada apenas')
from math import sqrt
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz do número {} é igual a {:.2f}'.format(num, raiz))

print()
# importar apenas o sqrt(calcular a raiz quadrada), e o floor(arredondar pra baixo)
print('Calcular a raiz quadrada e arredondar pra baixo')
from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz do número {} é igual a {:.2f}'.format(num, floor(raiz)))

#-----------------------------------------------------------------------------------------

# importar random(Números aleatorios)
print()
print('Número aleátorio(Números reais de 0 até 1)')
import random
num = random.random()
print(num)

print()
print('Número aleátorio(Números interios)')
import random
num = random.randint(1, 10)
print(num)

 