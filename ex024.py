'''Crie um programa que leia o nome de uma cidade e diga se ela começa ou não
com o nome "SANTO"'''
c = str(input('Digite o nome de uma cidade: \n')).strip()
b = c.capitalize().find('Santo')

if b == 0:
    print('O nome da cidade começa com Santo!')
else:
    print('O nome da cidade não começa com Santo!')
