# Primeiros passos com o Python 3

## Tipos primitivos

- `int` -> números inteiros
- `float` -> números reais
- `bool` -> booleano [`True`, `False`]
- `str` -> string -> caracteres

## Formato de variáveis dentro de strings [Python 3]

- Usar a função format()
    - `('string qualquer {} com {} variáveis {}'.format(var0, var1, var2))`
- Também é possível numerar as máscaras{}, sempre começando a contagem de 0
    -  `('string qualquer {2} com {0} variáveis {1}'.format(var0, var1, var2))`

## Operadores Aritméticos

- Adição: *`+`*
- Subtração: *`-`*
- Multiplicação: *`*`*
- Divisão: *`/`*
- Potência: *`**`*
- Divisão Inteira: *`//`*
- Resto da Divisão [Módulo]: *`%`*
- Operador de igualdade: *`==`*

### Ordem de Precedência

- 1: Parênteses: `()`
- 2: Potência: `**`
- 3: Multiplicação, divisão, divisão inteira e resto: `*`, `/`, `//` e `%`
- 4: Adição e subtração: `+`, `-`

## Módulos

- `import modulo` -> todas as funcionalidades do módulo
- `from modulo import funcionalidade` -> importa só uma funcionalidade específico

- `math`
    - `ceil` (arredonda pra cima)
    - `floor` (arredonda pra baixo)
    - `trunc` (ignora casa decimal sem arredondamento)
    - `pow` (potência)
    - `sqrt` (raiz quadrada)
    - `factorial` (fatorial)