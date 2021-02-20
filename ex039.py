'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
-se ele ainda vai se alistar ao serviço militar.
-Se é a hora de se alistar.
- Se passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou se passou do prazo.'''
from datetime import date
anoatual = date.today().year
nascimento = int(input('Digite o ano do seu nascimento: \n'))
print('''Digite:
1 - Masculino:
2 - Feminino''')
sexo = int(input())
idade = anoatual - nascimento
falta = 18 - idade
alistamento = anoatual + falta

if idade < 18 and sexo == 1:
    print('Você nasceu em {}, então você tem {} anos em {}!'.format(nascimento, idade, anoatual))
    print('Você ainda vai se alistar no serviço militar daqui {} anos!'.format(falta))
    print('Seu alistamento será em {}!'.format(alistamento))
elif idade == 18 and sexo == 1:
    print('Você nasceu em {}, então você tem {} anos em {}!'.format(nascimento, idade, anoatual))
    print('Já está na hora de você se alistar no serviço militar!')
elif idade > 18 and sexo == 1:
    print('Você nasceu em {}, então você tem {} anos em {}!'.format(nascimento, idade, anoatual))
    print('Já passou {} anos do tempo de você se alistar no serviço militar!'.format(idade - 18))
    print('Seu alistamento foi em {}!'.format(anoatual - (idade - 18)))
else:
    print('Você nasceu em {}, então você tem {} anos em {}!'.format(nascimento, idade, anoatual))
    print('Você não precisa fazer o alistamento militar obrigátorio por ser mulher!')