## Faça um programa que leia um ângulo qualquer e mostre na tela
## o valor do seno, cosseno e tangente desse ângulo.

'''
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
'''
# import math
from math import radians, sin, cos, tan

angulo = float(input('Digite o ângulo: '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('O Angulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
print('O Angulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
print('O Angulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))
