## Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o valor do salário em reais: R$'))

aumento = salario + (salario * 0.15)

print('O salario de R${:.2f} após o aumento de 15% passa a ser de R${:.2f}'.format(salario, aumento))