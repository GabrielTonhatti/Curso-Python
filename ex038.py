'''Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais'''

n = int(input('Digite um valor inteiro qualquer: \n'))
n2 = int(input('Digite outro valor inteiro qualquer: \n'))

if n > n2:
    print('O primeiro valor {} é maior!'.format(n))
elif n2 > n:
    print('O segundo valor {} é maior!'.format(n2))
else:
    print('Não existe valor maior, os dois valores são iguais!')