'''Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual a base de conversão:
1 para binário
2 para octal
3 para hexadecimal'''
num = int(input('Digite um número inteiro: \n'))
print('''Escolha uma das dases para a conversão:
1 - Binário:
2 - Octal:
3 - Hexadecimal:''')
opcao = int(input())

if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}!'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}!'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}!'.format(num, hex(num)[2:].upper()))
else:
    print('Opção Inválida!')