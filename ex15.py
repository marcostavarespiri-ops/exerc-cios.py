dias = int(input('Por quantos dias você usou o carro alugado?: '))
km = float(input('Quantos km você rodou?: '))

total = dias * 60 + km * 0.15

print(f'O valor a ser pago pelo aluguel do carro é de R${total:.2f}')
