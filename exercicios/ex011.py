## Faça um programa que leia a largura e a altura de uma parede em metros, 
## calcule a sua área e a quantidade de tinta necessária para pintá-la, 
## sabendo que cada litro de tinta pinta uma área de 2m²(2 metros quadrados)

altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))

metroQuadrado = altura * largura

print('Sua parede tem {:.0f}m². Você precisará de {:.2f} litros de tinta. '.format(metroQuadrado, metroQuadrado/2))