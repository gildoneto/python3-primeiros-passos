# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nomeCompleto = str(input('Digite seu nome completo: ')).strip()

print('NOME TEM SILVA? {}'.format( 'SILVA' in nomeCompleto.upper()))

# posicaoSilva = nomeCompleto.find('SILVA')
# tamSilva = posicaoSilva + 5

# if posicaoSilva >= 0:
#     print('NOME TEM', nomeCompleto[posicaoSilva: tamSilva])
# else:
#     print('NOME NÃO TEM SILVA')
