'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0:
REPROVADO
-Média entre 5.0 e 6.9:
RECUPERAÇÃO
-Média 7.0 ou superior:
APROVADO'''
nota = float(input('Digite a primeira nota do aluno: \n'))
nota2 = float(input('Digite a segunda nota do aluno: \n'))
media = (nota + nota2) / 2

if media < 5:
    print('Tirando {:.2f} e {:.2f}, a média do aluno é {:.2f}!'.format(nota, nota2, media))
    print('Aluno \033[31mREPROVADO\033[m!')
elif media >= 5 and media <= 6.9:
    print('Tirando {:.2f} e {:.2f}, a média do aluno é {:.2f}!'.format(nota, nota2, media))
    print('Aluno \033[33mRECUPERAÇÃO\033[m!')
else:
    print('Tirando {:.2f} e {:.2f}, a média do aluno é {:.2f}!'.format(nota, nota2, media))
    print('Aluno \033[32mAPROVADO\033[m!')
