d = float(input('Digite um valor para ser convertido em dólar: '))
r = float(input('Digite um valor em dólar para ser convertido em real: '))
dolar = d / 5.20
real = r * 5.20
print(f'O valor em R${d} convertido em dolar é: ${dolar:.2f}')
print(f'O valor de {r} convertido em real é: R${real:.2f}')