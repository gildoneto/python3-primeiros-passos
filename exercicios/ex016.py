## Crie um programa que leia um número Real qualquer pelo teclado e mostre
## na tela a sua porção inteira.
## Ex: Digite um número: 6.127 | O número 6.127 tem a parte inteira 6.

from math import trunc

num = float(input('Digite um numero real: '))

print('A parte inteira do número {} é {}'.format(num, trunc(num)))

## nesse caso a função int() também tem o mesmo comportamento do trunc()
# print('A parte inteira do número {} é {}'.format(num, int(num)))