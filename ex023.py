'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um
dos digitos separados.
Ex:
Digite um número: 1834

unidade: 4
dezena: 3
centena: 8
milhar: 1'''

n = int(input('Digite um número de 0 até 9999: \n'))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print()
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))