# Crie um programa que leia o nome de uma cidade e diga 
# se ela começa ou não com o nome "SANTO".

cidade = input('Digite o nome da sua cidade: ')

splitCidade = cidade.split()[0].upper()

if splitCidade == 'SANTO':
    print('Começa com a palavra', splitCidade)
else:
    print('NÃO começa com a palavra SANTO')
