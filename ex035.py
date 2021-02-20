'''Desenvolva um programa que leia o comprimemto de três retas e diga ao usuário
se elas podem ou não formar um triângulo.'''
print('-=' * 13)
print(' ANALISADOR DE TRIÂNGULO!')
print('-=' * 13)
reta = float(input('Digite o comprimento da primeira reta: \n'))
reta2 = float(input('Digite o comprimento da segunda reta: \n'))
reta3 = float(input('Digite o comprimento da terceira reta: \n'))

if reta < reta2 + reta3 and reta2 < reta + reta3 and reta3 < reta + reta2:
    print('Com os 3 comprimentos pode se formar um triângulo!')
else:
    print('Não pode se formar um triângulo com esses 3 comprimentos!')
