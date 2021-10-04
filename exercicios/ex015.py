## Aluguel de Carros
## Cotação: R$60 por dia e R$0,15 por Km rodado

dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Rodou quantos Km? '))

total = (60 * dias) + (0.15 * km)

print('O valor a pagar pelo aluguel é de R${:.2f}'.format(total))