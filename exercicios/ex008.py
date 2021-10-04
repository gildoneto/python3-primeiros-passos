## Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

valorDigitado = int(input('Digite um valor: '))

cent = valorDigitado * 100
mili = valorDigitado * 1000

print('{} metro(s) é igual a {} centímetros ou a {} milímetros.'.format(valorDigitado, cent, mili))