# Crie um programa que leia o nome de uma cidade e diga 
# se ela começa ou não com o nome "SANTO".

cidade = str(input('Digite o nome da sua cidade: ')).strip()

print(cidade[:5].upper() == 'SANTO')

# splitCidade = cidade.split()[0].upper()

# if splitCidade == 'SANTO':
#     print('Começa com a palavra', splitCidade)
# else:
#     print('NÃO começa com a palavra SANTO')
