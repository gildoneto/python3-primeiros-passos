# Escreva um programa faça o computador pensar em um
# numero inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.

# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

numMaquina = random.randint(0, 5)

numUsuario = int(input('Adivinhe que numero o computador está pensando agora entre 0 e 5: '))

if numUsuario == numMaquina:
    print('\nWOW!! Você acertou. O Computador tinha pensado justamente no numero {}.'.format(numUsuario))
else:
    print('\nErrou. Você digitou {}, e o computador pensou no número {}'.format(numUsuario, numMaquina))

print('GAME OVER')
