# faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada.
n = int(input('Digite um número qualquer: '))
print('Tabuada do {}!'.format(n))
print('-' * 12)
for i in range(1, 11):
    print('{} X {:2} = {}'.format(n, i, n * i))

print('-' * 12)
    