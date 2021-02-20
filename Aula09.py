frase = 'Curso em Vídeo Python'
print(frase[9::3]) #mostrar da nona letra em diante pulando de 3 em 3
print(len(frase)) #mostrar o comprimento da frase
print(frase.count('V')) #mostrar quantas letras "V" tem na frase
print(frase.find('deo')) # encontrar na onde começa a palavra "deo"
print(frase.find('Android')) # encontrar na onde começa a palavra "Android"
print('Curso' in frase) # Dizer se tem a palavra "Curso" na frase
print(frase.replace('Python', 'Android')) # substitiur a palavra "Python" pela palavra "Android"
print(frase)
print(frase.upper()) #colocar todas as letras em maisculo
print(frase.lower()) #colocar todas as letras em minusculo
print(frase.capitalize()) # colocar apenas a primeira letra da primeira palavra em maiusculo
print(frase.title()) # colocar a primeira letras de cada palavra em maiusculo
frase = '   Aprenda Python  '
print(frase)
print(frase.strip()) # remover espaços inuteis
print(frase.rstrip()) # remover espaços inuteis do lado direito
print(frase.lstrip()) # remover espaços inuteis do lado esquerdo
frase = 'Curso em Vídeo Python' 
print(frase.split()) # dividir as palavras, deixando cada frase separada, gerando uma lista nova
frase = frase.split()
print('-'.join(frase)) # juntar as palavras em uma so novamente, com o "-" como separação