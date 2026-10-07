import random
a1 = (input('Um professor me deu uma proesa tarefa \n de sortear 1 de seus 4 alunos para apagar seu quadro. \n Me fale o nome do 1º: '))
a2 = (input('Agora, do segundo: '))
a3 = (input('Do 3º: '))
a4 = (input('E por último, do 4º: '))
lista = [a1, a2, a3, a4]

vencedor = random.choice(lista) 

print(f'E o aluno sorteado foi, {vencedor}')
