## Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

produto = float(input('Digite o valor do produto em reais: R$'))

#desconto = produto - (produto * 0.05)
desconto = produto - (produto * 5 / 100)

print('O produto de valor R${:.2f} após o desconto de 5% passa a ser R${:.2f}'.format(produto, desconto))