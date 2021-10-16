# Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento.

# Para salários superiores a R$1.250,00, calcule um aumento de 10%.

# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite seu Salario: '))

if salario <= 1250:
    print('Seu salario de R${:.2f} aumentara 15%. Novo salario: R${:.2f}'.format(salario, salario + salario * 0.15))
else:
    print('Seu salario de R${:.2f} aumentara 10%. Novo salario: R${:.2f}'.format(salario, salario + salario * 0.10))
