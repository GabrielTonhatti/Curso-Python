# Faça um algoritmo que leia a largura e a altura de uma parede em metros, calcule a sua área
# e a quantidade de tinta necessaria para pintá-la, sabendo que cada litro de tinta pinta
# uma área de 2m².
l = float(input('Digite a largura da parede em metros: '))
A = float(input('Digite a altura da parede em metros: '))
a = A * l
print('Sua parede tem a dimensão de {}X{} e sua área é de {:.2f}m²!'.format(l, A, a))
print('Você vai precisar de {:.2f}l de tinta para pintar a parede!'.format(a / 2))
