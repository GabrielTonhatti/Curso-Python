'''Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas;
- O nome com todas as letras minúsculas;
- Quantas letras tem ao todo(sem considerar espaços);
- Quantas letras tem o primeiro nome.'''
nome = str(input('Digite seu nome completo: \n')).strip()
print()
print('O nome com todas as letras em maiúsculas: \n {}'.format(nome.upper()))
print('O nome com todas as letras em minúsculas: \n {}'.format(nome.lower()))
print('O nome completo tem {} letras'.format(len(nome)-nome.count(' ')))
print('O primeiro nome tem {} letras'.format(nome.find(' ')))
print()

# segunda forma de fazer o ultimo print
separa = nome.split()
print('O primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))