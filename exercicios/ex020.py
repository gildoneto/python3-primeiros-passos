## O mesmo desafio do professor anterior quer sortear a ordem de apresentacao de trabalhos dos alunos.
## Faça um program que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

a1 = str(input('Aluno 1: '))
a2 = str(input('Aluno 2: '))
a3 = str(input('Aluno 3: '))
a4 = str(input('Aluno 4: '))

lista = [a1, a2, a3, a4]

random.shuffle(lista)

print('A ordem de apresentacao será: {}'.format(lista))