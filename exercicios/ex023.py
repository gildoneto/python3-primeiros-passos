# Faça um programa que leia um número de 0 a 9999 e mostre na tela 
# cada um dos dígitos separados

# Ex:
# Digite um número: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

milhar = input('Digite um número de 4 dígitos: ')

print("""
Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}
""".format(milhar[3],milhar[2],milhar[1],milhar[0]))