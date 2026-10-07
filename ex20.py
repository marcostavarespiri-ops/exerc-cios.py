import random
t1 = input('Nome do aluno de um trabalho: ')
t2 = input('Aluno do próximo trabalho: ')
t3 = input('Próximo: ')
t4 = input('Agora, o último: ')
lista = [t1, t2, t3, t4]

random.shuffle (lista)

print(f'A ordem de apresentação dos trabalhos, será: {lista}')