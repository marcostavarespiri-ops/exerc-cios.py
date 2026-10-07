import math
angulo = float(input('Digite o valor do ângulo de um triângulo: '.replace(',','.')))
angulo_convertido = math.radians (angulo)
seno = math.sin(angulo_convertido)
cosseno = math.cos(angulo_convertido)
tangente = math.tan(angulo_convertido)

print(f'O seu seno é igual a {seno}, o cosseno é {cosseno} e a tangente é {tangente}')



