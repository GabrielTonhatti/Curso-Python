'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''
n = int(input('Digite um número inteiro qualquer: \n'))
n2 = int(input('Digite outro número inteiro qualquer: \n'))
n3 = int(input('Digite outro número inteiro qualquer: \n'))

if n > n2 and n2 > n3:
    print('O maior número é o {}, e o menor é o {}!'.format(n, n3))
elif n2 > n and n > n3:
    print('O maior número é o {}, e o menor é o {}!'.format(n2, n3))
elif n3 > n and n > n2:
    print('O maior número é o {}, e o menor é o {}!'.format(n3, n2))
elif n3 > n2 and n2 > n:
    print('O maior número é o {}, e o menor é o {}!'.format(n3, n))
elif n2 > n3 and n3 > n:
    print('O maior número é o {}, e o menor é o {}!'.format(n2, n))
elif n > n3 and n3 > n2:
    print('O maior número é o {}, e o menor é o {}!'.format(n, n2))
elif n == n2 and n > n3:
    print('O maior número é o {}, e o menor é o {}!'.format(n2, n3))
elif n == n3 and n > n2:
    print('O maior número é o {}, e o menor é o {}!'.format(n, n2))
elif n2 == n3 and n3 > n:
    print('O maior número é o {}, e o menor é o {}!'.format(n2, n))
elif n == n2 and n3 > n:
    print('O maior número é o {}, e o menor é o {}!'.format(n3, n))
elif n == n3 and n2 > n:
    print('O maior número é o {}, e o menor é o {}!'.format(n2, n))
elif n3 == n2 and n > n2:
    print('O maior número é o {}, e o menor é o {}!'.format(n, n3))
else:
    print('Os números são todos iguais!')
