## Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.

valorDigitado = int(input('Digite um número: '))

print('O dobro de {} é {}. O triplo é {}, e raiz quadrada é {:.2f}'.format(valorDigitado, valorDigitado * 2, valorDigitado * 3, valorDigitado**(1/2)))