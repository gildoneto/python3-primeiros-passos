# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nomeCompleto = input('Digite seu nome completo: ').upper()

posicaoSilva = nomeCompleto.find('SILVA')
tamSilva = posicaoSilva + 5

if posicaoSilva >= 0:
    print('NOME TEM', nomeCompleto[posicaoSilva: tamSilva])
else:
    print('NOME NÃO TEM SILVA')