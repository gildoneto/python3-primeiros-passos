## Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

valorDigitado = int(input('Digite um valor: '))

cm = valorDigitado * 100
mm = valorDigitado * 1000

print('{} metro(s) é igual a {} centímetros ou a {} milímetros.'.format(valorDigitado, cm, mm))