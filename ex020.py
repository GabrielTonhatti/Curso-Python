'''O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''
import random
aluno = input('Primeiro aluno: \n')
aluno2 = input('Segundo aluno: \n')
aluno3 = input('Terceiro aluno: \n')
aluno4 = input('Quarto aluno: \n')
lista = [aluno, aluno2, aluno3, aluno4]
random.shuffle(lista)
print('A ordem dos alunos será {}'.format(lista))

from random import shuffle
aluno = input('Primeiro aluno: \n')
aluno2 = input('Segundo aluno: \n')
aluno3 = input('Terceiro aluno: \n')
aluno4 = input('Quarto aluno: \n')
lista = [aluno, aluno2, aluno3, aluno4]
shuffle(lista)
print('A ordem dos alunos será {}'.format(lista))
