'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usúario venceu ou perdeu.'''
from random import randint
from time import sleep

random = randint(0, 5)

print('-=-' * 20)
print('    Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
num = int(input('Em que número eu pensei? \n'))
print('PROCESSANDO...')
sleep(2)

if random == num:
    print('Parabéns você venceu!')
else:
    print('Você perdeu, eu pensei no número {} e não no número {}!'.format(random, num))
    