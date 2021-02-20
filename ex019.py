# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa
# que ajuda ele, lendo o nome deles e escrevendo o nome do escolhido .
import random
aluno = input('Primeiro aluno: \n')
aluno2 = input('Segundo aluno: \n')
aluno3 = input('Terceiro aluno: \n')
aluno4 = input('Quarto aluno: \n')
lista = [aluno, aluno2, aluno3, aluno4]
sorte = random.choice(lista)
print('O aluno sorteado foi {}'.format(sorte))

print()
print('Importando apenas o choice')
from random import choice
aluno = input('Primeiro aluno: \n')
aluno2 = input('Segundo aluno: \n')
aluno3 = input('Terceiro aluno: \n')
aluno4 = input('Quarto aluno: \n')
lista = [aluno, aluno2, aluno3, aluno4]
sorte = choice(lista)
print('O aluno sorteado foi {}'.format(sorte))
