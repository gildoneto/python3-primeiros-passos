cores = {
    'limpa':'\033[m',
    'azul':'\033[34m',
    'amarelo':'\033[33m',
    'peb':'\033[7;37;40m',
    'red':'\033[31m'
}

nome = 'Gildo'
print('Ola {}{}{}'.format(cores['red'], nome, cores['limpa']))