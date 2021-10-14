# tempo = int(input('Quantos anos tem seu carro? '))
# # print('carro novo' if tempo <= 3 else 'carro velho')
# if tempo <= 3:
#    print('carro novo')
# else:
#     print('carro velho')
# print('--FIM--')

#########################################################################

# nome = str(input('Seu nome: '))
# if nome == 'Gildo':
#     print('Nome de Avô')
# print('Bem vindo, {}!'.format(nome))

#########################################################################

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))

media = (n1 + n2)/2
print('Media foi {:.1f}'.format(media))

if media >= 6.0:
    print('APROVADO!')
else:
    print('REPROVADO!')