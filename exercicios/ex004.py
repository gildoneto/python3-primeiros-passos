## Faça um programa que leia algo pelo teclado e mostre na tela
## o seu tipo primitivo e todas as informações possíveis sobre ele.

valorDigitado = input('Digite algo: ')

print('Valor digitado: {}'.format(valorDigitado))
print('Tipo primitivo: {}'.format(type(valorDigitado)))
print('É alfabético? {}'.format(valorDigitado.isalpha()))
print('É numérico? {}'.format(valorDigitado.isnumeric()))
print('É alfanumérico? {}'.format(valorDigitado.isalnum()))
print('Tem espaços? {}'.format(valorDigitado.isspace()))
print('Todas as letras maiúsculas? {}'.format(valorDigitado.isupper()))
print('Todas as letras minúsculas? {}'.format(valorDigitado.islower()))
print('Está capitalizada? {}'.format(valorDigitado.istitle()))
