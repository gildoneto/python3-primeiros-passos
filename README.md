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

## Manipulando Texto

**`frase = 'Curso em Vídeo Python'`**

- Fatiamento
    ```python
    frase = 'Curso em Vídeo Python'

    frase[9] ==> 'V'
    frase[9:13] ==> 'Víde'
    frase[9:14] ==> Vídeo
    frase[9:21] ==> Vídeo Python
    frase[9:21:2] ==> VdoPto
    frase[:5] ==> Curso
    frase[15:] ==> Python
    frase[9::3] ==> Veph
    ```

- Análise
    ```python
    frase = 'Curso em Vídeo Python'

    len(frase) ==> 21
    frase.count('o') ==> 3
    frase.count('o', 0, 13) ==> 1
    frase.find('deo') ==> 11
    frase.rfind('n') ==> 20
    frase.find('Android') ==> -1
    'Curso' in frase ==> True
    ```

- Transformacão
    ```python
    frase = 'Curso em Vídeo Python'

    frase.replace('Python', 'Android') ==> frase == 'Curso em Vídeo Android'
    frase.upper() ==> frase == 'CURSO EM VIDEO PYTHON'
    frase.lower() ==> frase == 'curso em video python'
    frase.capitalize() ==> frase == 'Curso em video python'
    frase.title() ==> frase == 'Curso Em Video Python'
    ```
    ```python
    frase = '   Aprenda Python  '

    frase.strip() ==> frase == 'Aprenda Python'
    frase.rstrip() ==> frase == '   Aprenda Python'
    frase.lstrip() ==> frase == 'Aprenda Python  '
    ```

- Divisão
    ```python
    frase = 'Curso em Vídeo Python'

    frase.split() ==> frase == ['Curso', 'em', 'Vídeo', 'Python']
    ```

- Junção
    ```python
    frase = ['Curso', 'em', 'Vídeo', 'Python']

    '-'.join(frase) ==> frase == 'Curso-em-Vídeo-Python'
    ```

## Condições

### Condição Simples

```python
if media >= 6.0:
    print('APROVADO!')
```

### Condição Composta

```python
if media >= 6.0:
    print('APROVADO!')
else:
    print('REPROVADO!')
```

### Condição Simplificada

```python
print('APROVADO!' if media >= 6 else 'REPROVADO!')
```

## Cores no Terminal

### ANSI Escape Sequence

Começa sempre com um contrabarra `\`

```python
'\033[(style; text; background)m'
'\033[0:33:44m'
'\033[m' # limpa
```

`style`
    - 0 - None
    - 1 - Bold
    - 4 - Underline
    - 7 - Negative

`text`
    - 30 - White
    - 31 - Red
    - 32 - Green
    - 33 - Yellow
    - 34 - Blue
    - 35 - Magenta
    - 36 - Cyan
    - 37 - Gray

`back`
    - 40 - White
    - 41 - Red
    - 42 - Green
    - 43 - Yellow
    - 44 - Blue
    - 45 - Magenta
    - 46 - Cyan
    - 47 - Gray

