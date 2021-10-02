#_| inputs são considerados strings
# testeTipo01 = input('Digite um numero: ')
# print(type(testeTipo01))

#_| pra que ele seja armazenado com int
#_| é necessário colocar o input dentro da funcao int()
# testeTipo02 = int(input('Digite um numero:  '))
# print(type(testeTipo02))

#_| somando dois números com a função int
number01 = int(input('number 01: '))
number02 = int(input('number 02: '))
sum = number01 + number02
print('O total da soma é', sum)

#_| somando dois números sem a função int
#_| teremos uma concatenação ao invés de uma soma
number03 = input('number 03: ')
number04 = input('number 04: ')
sum = number03 + number04
# print('Neste caso você está concatenando os números', number03, 'e', number04, 'que vai resultar em:', sum)
#_| existe uma forma melhor de adicionar variáveis dentro de uma string.
#_| usando o a funcao format() e dentro da string usar a mascara {}
print('Neste caso você está concatenando os números {} e {} que vai resultar em: {}'.format(number03, number04, sum))
