 ## Faça um programa que leia um número inteiro e mostra na teela o seu sucessor e seu atencessor

valorDigitado = int(input('Digite um número: '))
antecessor = valorDigitado - 1
sucessor = valorDigitado + 1

print('O valor antecessor a {} é {} e o sucessor é {}'.format(valorDigitado, antecessor, sucessor))