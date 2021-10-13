# Crie um programa que leia o nome completo de uma pessoa e mostre:
nomeCompleto = input('Digite seu nome completo: ')
# O nome com todas as letras maiúsculas
print('Letras Maiusculas: ', nomeCompleto.upper())
# O nome com todas minúsculas
print('Letras Minusculas: ', nomeCompleto.lower())
# Quantas letras ao todo (sem considerar espaços)
print('Numero de letras sem espacos: ', len(nomeCompleto.replace(' ', '')))
# Quantas letras tem o primeiro nome
print('Numero de letras do primeiro nome: ', len(nomeCompleto.split()[0]))