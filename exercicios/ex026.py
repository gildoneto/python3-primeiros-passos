# Faça um programa que leia uma frase pelo teclado e mostre:
frase = input('Formule uma frase: ')
# Quantas vezes aparece a letra "A"
print('A letra "A" aparece',frase.count('A'), 'vezes')
# Em que posição ela aparece a primeira vez
print('Primeira posicao palavra "A":', frase.find('A'))
# Em que posição ela aparece a última vez.
print('Ultima posicao palavra "A":', frase.rfind('A'))
