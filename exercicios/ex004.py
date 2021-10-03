## Faça um programa que leia algo pelo teclado e mostre na tela
## o seu tipo primitivo e todas as informações possíveis sobre ele.

valorDigitado = input('Digite algo: ')
alfa = valorDigitado.isalpha()
numeric = valorDigitado.isnumeric()
alfanum = valorDigitado.isalnum()
print('O valor foi {}. É alfabético? {}. É numérico? {}. É alfanumérico? {}.'.format(valorDigitado, alfa, numeric, alfanum))