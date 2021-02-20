'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7,00 por cada km acima do limite'''
velo = int(input('Qual a velocidade do carro? Km \n'))
multa = float((velo - 80) * 7)

if velo > 80:
    print('A velocidade maxima permitida é de 80Km/h!')
    print('Você foi multado por excesso de velocidade, a multa é de R${:.2f}!'.format(multa))
else:
    print('Você está dentro da velocidade permitida, tenha um Bom dia!')