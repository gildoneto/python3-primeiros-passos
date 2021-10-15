# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

maior = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
num3 = int(input('Digite o terceiro numero: '))

if num2 > maior:
    maior = num2

if num3 > maior:
    maior = num3

print('O maior número é ', maior)