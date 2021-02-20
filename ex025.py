'''Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.'''
n = str(input('Digite seu nome completo: \n')).strip()
n = n.upper()
t = 'SILVA' in n

if t == True:
    print('Você tem Silva no seu nome!')
else:
    print('Você não tem Silva no seu nome!')