## Faça um programa que leia o comprimento do cateto oposto e
## do cateto adjacente de um triângulo retângulo, calcule e
## mostre o comprimento da hipotenusa.

#import math

from math import hypot

oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))

# # maneira matemática, sem importar o math
# hipotenusa = (oposto ** 2 + adjacente ** 2) ** (1/2)

hipotenusa = hypot(oposto, adjacente)

print('A hipotenusa mede {:.2f}'.format(hipotenusa))