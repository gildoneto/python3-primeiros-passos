# Escreva um programa que leia a velocidade de um carro.

# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.

# A multa vai custar R$7,00 por cada Km acima do limite.

multa = 7.0

Km = int(input('Velocidade em Km: '))

if Km > 80:
    print('Você ultrapassou o limite, sua multa é de R${:.2f}'.format((Km - 80) * multa))
