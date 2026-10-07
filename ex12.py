n = int(input('Digite um valor entre 50 e 200, de quanto pagaria por uma calça: '))
if n < 50 or n > 200:
    while True:
            n = int(input('Digite um valor válido entre 50 e 200: '))
            if n >= 50 and n <=200:
                 break
a =int(input('Agora, digite um número de 1 a 100 para saber qual será o seu desconto: '))
if a < 1 or a >100:
    while True:
            a = int(input('Digite um número válido de 1 a 100: '))
            if a >= 1 and a <=100:
                  break
if n >= 50 and n <= 200 and a >= 1 and a <=50:
    print(f'Você pagará o valor cheio de R${n:.2f} pela calça')
if n >= 50 and n <= 200 and a >= 51 and a <=100:
    print(f'Seu desconto será de 5%, então pagará R${n-(n*0.05):.2f} pela calça')