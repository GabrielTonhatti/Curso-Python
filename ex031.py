'''Desenvolva um programa que pergunte a distância da viagem em km. Calcule o preço da passagem,
cobrando R$ 0,50 por km para viagens de até 200km e R$ 0,45 para viagens mais longas.'''
distan = int(input('Digite a dinstância que deseja viajar: \n'))

if distan <= 200:
    total = distan * 0.50
    print('O preço da viagem vai ser R${:.2f}!'.format(total))
else:
    total = distan * 0.45
    print('O preço da viagem vai ser R${:.2f}!'.format(total))