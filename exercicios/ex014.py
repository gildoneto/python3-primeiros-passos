## Conversor de Temperaturas

celsius = float(input('Digite a temperatura em C: '))
#fahrenheit = (celsius * 9/5) + 32
fahrenheit = 9 * celsius / 5 + 32

print('{:.2f} graus Celsius equivale a {:.2f} graus em Fahrenheit'.format(celsius, fahrenheit))