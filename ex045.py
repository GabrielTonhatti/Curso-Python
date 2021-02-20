'''Crie um programa que faça o computador jogar jakenpô com você.'''

from random import randint

pc = randint(1, 3)
print('-='*15)
print('       JOGO DO JAKENPÔ!')
print('-='*15)
jogador = int(input('Digite 1-Pedra, 2-Papel ou 3-Tesoura: \n'))

if pc == 1:
    jogada = 'Pedra'
elif pc == 2:
    jogada = 'Papel'
elif pc == 3:
    jogada = 'Tesoura'

if jogador == 1:
    jogada2 = 'Pedra'
elif jogador == 2:
    jogada2 = 'Papel'
elif jogador == 3:
    jogada2 = 'Tesoura'

print('O Computador escolheu {}!'.format(jogada))
print('Você escolheu {}!'.format(jogada2))

if pc == jogador:
    print('Empate você e o computador escolheram {}!'.format(jogada))
elif pc == 1 and jogador == 2:
    print('Parabéns você venceu!')
elif pc == 3 and jogador == 1:
    print('Parabéns você venceu!')
elif pc == 2 and jogador == 3:
    print('Parabéns você venceu!')
elif pc == 1 and jogador == 3:
    print('Você perdeu! O computador ganhou de você!')
elif pc == 2 and jogador == 1:
    print('Você perdeu! O computador ganhou de você!')
elif pc == 3 and jogador == 2:
    print('Você perdeu! O computador ganhou de você!')
