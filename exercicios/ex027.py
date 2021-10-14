# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
# o primeiro e o último nome separadamente.

# Ex: Ana Maria de Souza
# primeiro = Ana
# ultimo = Souza

nomeCompleto = input('Digite seu nome completo: ')

numPalavras = len(nomeCompleto.split())

print("""
Primeiro Nome: {}
Último Nome: {}
""".format(nomeCompleto.split()[0],nomeCompleto.split()[numPalavras-1]))