'''Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar qual tipo de triângulo será formado?
-Equilátero: todos os lados iguais
-isósceles: dois lados iguais
-Escaleno: todos os lados diferentes'''

lado = float(input('Digite o comprimento do primeiro lado: \n'))
lado2 = float(input('Digite o comprimento do segundo lado: \n'))
lado3 = float(input('Digite o comprimento do terceiro lado: \n'))

if lado < lado2 + lado3 and lado2 < lado + lado3 and lado3 < lado2 + lado:
    if lado == lado2 and lado == lado3:
        print('Pode ser formar um triângulo Equilátero!')
    elif lado == lado2 or lado == lado3 or lado3 == lado2:
        print('Pode se formar um triângulo Isósceles!')
    else:
        print('Pode se formar um triângulo Escaleno!')
else:
    print('Não pode se formar um triângulo com esses três comprimentos!')