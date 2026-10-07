a = float(input('Digite um valor para receber uma recompensa: '))
if a <= 1:
    print(f'Você ficará azarado por 2 dias seguidos!!')
elif a > 1 and a <= 4:
    print(f'Você recerá uma boa mensagem de alguém distante daqui 7 dias')
elif a > 4 and a <=8:
    print(f'Você não poderá falar por 1 dia inteiro')
elif a > 8 and a <= 10:
    print(f'Nada! Parabéns')
elif a >= 10:
    print(f'Você nunca mais mentirá de novo na vida')