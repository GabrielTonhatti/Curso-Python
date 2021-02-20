'''Faça um programa que leia uma frase pelo teclado e mostre:

- Quantas vezes aparece a letra "A";
- Em que posição ela aparece pela primeira vez;
- Em que posição ela apareceu a última vez.'''

n = str(input('Digite uma frase: \n')).strip()
n = n.upper()

v = n.count('A')
p = n.find('A') + 1
u = n.rfind('A') + 1

print('A letra "A" apareceu {} vezes na frase!'.format(v))
print('A primeira vez que a letra "A" apareceu foi na posição {}!'.format(p))
print('A última vez que a letra "A" apareceu na frase foi na posição {}!'.format(u))