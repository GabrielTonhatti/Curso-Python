# Escreva um programa que leia um valor em metros e a exiba convertida em cm e milimetros
metros = float(input('Digite um valor em metros: '))
print('O valor {}m em cm é {:.0f}cm!'.format(metros, 100 * metros))
print('O valor {}m em milimetros é {:.0f}mm!'.format(metros, 1000 * metros))
