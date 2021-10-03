## Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.

valorDigitado = int(input('Digite um número: '))

dobro = valorDigitado * 2
triplo = valorDigitado * 3
raiz = valorDigitado**(1/2)

print('O dobro de {} é {}. O triplo é {}, e raiz quadrada é {}'.format(valorDigitado, dobro, triplo, raiz))