frase = input('Digite uma frase rápida: ')

len(frase) (fatiar a frase inteira. Ele considera o texto todo que está escrito)

frase.count('o') (quantas letras 'o' possue na frase)

frase.find('deo') (mostra onde estará "deo" na frase)

frase.find ('android') (por ex: nesse caso, se na resposta, se vc usar o "android" para procurar palavras como android no texto e ele retornar -1, significa que 'android' não existe')

frase.replace('Python', 'Android') (Substitui Python por android)

print (f'Essa frase, vai aparecer como: {frase[3::2]}')
