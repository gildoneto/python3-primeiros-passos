# Desenvolva um programa que pergunta a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de
# até 200Km e R$0,45 para viagens mais longas.

distancia = int(input('Digite a distancia: '))

if distancia <= 200:
    print('Para {}Km de viagem sua passagem será R${:.2f}.'.format(distancia, distancia * 0.50))
else:
    print('Para {}Km de viagem sua passagem será R${:.2f}.'.format(distancia, distancia * 0.45))
