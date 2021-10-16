# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date

ano = int(input('Digite o ano: '))

if ano == 0:
    ano = date.today().year
if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
    print('{} É um ano bissexto'.format(ano))
else:
    print('{} Não é bissexto'.format(ano))