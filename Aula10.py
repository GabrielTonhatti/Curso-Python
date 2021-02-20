n = float(input('Digite a primeira nota: \n'))
n2 = float(input('Digite a segunda nota: \n'))
media = (n + n2) / 2

if media >= 6:
    print('Aluno aprovado com média {:.1f}!'.format(media))
else:
    print('Aluno reprovado com média {:.1f}!'.format(media))