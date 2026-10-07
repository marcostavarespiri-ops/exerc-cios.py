import math
ca = float(input('Digite o valor de um cateto adjacente: '
.replace(',','.')))
co = float(input('Agora, do cateto oposto: '.replace(',', '.')))
hipotenusa = math.trunc(math.hypot(ca, co))
print(f'O valor da hipotenusa é: {math.trunc(hipotenusa)}') 