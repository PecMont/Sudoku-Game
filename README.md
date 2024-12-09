# Sudoku 
Este código em Python gera, resolve e permite jogar um jogo de Sudoku.

## Funções

### (def gerar_sudoku()

Este código em Python gera, resolve e permite jogar um jogo de Sudoku. Abaixo, está a documentação detalhada das funções e como o código funciona em geral.
```py
def gerar_sudoku():
    # Inicializa um tabuleiro vazio
    tabuleiro = [[0 for _ in range(9)] for _ in range(9)]

    # Preenche as caixas diagonais
    for i in range(0, 9, 3):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(nums)
        for j in range(3):
            for k in range(3):
                tabuleiro[i + j][i + k] = nums.pop()

    # Resolve o quebra-cabeça
    resolver_sudoku(tabuleiro)

    # Remove alguns números do tabuleiro para criar um quebra-cabeça
    celulas_vazias = 20  # Número de células vazias no quebra-cabeça
    while celulas_vazias > 0:
        linha = random.randint(0, 8)
        coluna = random.randint(0, 8)
        if tabuleiro[linha][coluna] != 0:
            tabuleiro[linha][coluna] = 0
            celulas_vazias -= 1

    return tabuleiro
```
#### Descrição 
- Cria uma tabuleiro vazio.
- Preenche as caixas diagonais 3x3 com números aleatórios de 1 a 9.
- Chama a função _resolver_sudoku()_ para preencher o resto do tabuleiro de forma válida.
- Remove 20 números aleatórios para criar células vazias, permitindo que o jogador resolva o quebra-cabeça.
- 
### resolver_sudoku(tabuleiro)
Esta função resolve o tabuleiro de Sudoku recursivamente utilizando backtracking.
```py
def resolver_sudoku(tabuleiro):
    # Encontra a próxima célula vazia
    linha, coluna = encontrar_celula_vazia(tabuleiro)
    if linha == -1:  # Se não houver mais células vazias, o quebra-cabeça está resolvido
        return True

    # Tenta cada valor possível para a célula vazia
    for num in range(1, 10):
        if movimento_valido(tabuleiro, linha, coluna, num):
            # Coloca o número na célula vazia
            tabuleiro[linha][coluna] = num

            # Resolve recursivamente o quebra-cabeça
            if resolver_sudoku(tabuleiro):
                return True

            # Se o quebra-cabeça não puder ser resolvido com este número, remova-o
            tabuleiro[linha][coluna] = 0

    # Se nenhum dos números possíveis funcionar, faça um retrocesso
    return False
```

#### Parâmetros:

- _tabuleiro:_ O tabuleiro de Sudoku atual, representado por uma matriz 9x9.
#### Descrição:

- Encontra a próxima célula vazia usando a função _encontrar_celula_vazia()_.
- Para cada célula vazia, tenta números de 1 a 9.
- Verifica se o número é válido na posição usando movimento_valido().
- Se o número é válido, o coloca no tabuleiro e chama a função recursivamente.
- Caso nenhum número funcione, retorna False e faz o retrocesso.
#### Retorno:

_True_ se o tabuleiro foi resolvido com sucesso, _False_ caso contrário.
### encontrar_celula_vazia(tabuleiro)
Esta função encontra a próxima célula vazia no tabuleiro.
```py
def encontrar_celula_vazia(tabuleiro):
    for linha in range(9):
        for coluna in range(9):
            if tabuleiro[linha][coluna] == 0:
                return linha, coluna
    return -1, -1  # Se não houver mais células vazias, retorne -1
```

#### Parâmetros:

- tabuleiro: O tabuleiro de Sudoku.
#### Descrição:

- Itera sobre o tabuleiro procurando por uma célula com valor 0 (vazia).
- Retorna as coordenadas da célula vazia (linha, coluna).
#### Retorno:

Retorna a posição da célula vazia _(linha, coluna)_ ou _(-1, -1)_ se não houver células vazias.
### movimento_valido(tabuleiro, linha, coluna, num)
Verifica se um número pode ser colocado em uma posição específica do tabuleiro.
```py
def movimento_valido(tabuleiro, linha, coluna, num):
    # Verifica se o número já está na linha
    for i in range(9):
        if tabuleiro[linha][i] == num:
            return False

    # Verifica se o número já está na coluna
    for i in range(9):
        if tabuleiro[i][coluna] == num:
            return False

    # Verifica se o número já está na caixa 3x3
    inicio_linha_caixa = (linha // 3) * 3
    inicio_coluna_caixa = (coluna // 3) * 3
    for i in range(inicio_linha_caixa, inicio_linha_caixa + 3):
        for j in range(inicio_coluna_caixa, inicio_coluna_caixa + 3):
            if tabuleiro[i][j] == num:
                return False

    return True
```

#### Parâmetros:

- tabuleiro: O tabuleiro de Sudoku.
- linha: A linha da célula a ser verificada.
- coluna: A coluna da célula a ser verificada.
- num: O número a ser verificado.
#### Descrição:

Verifica se o número não aparece na mesma linha, coluna ou na caixa 3x3 correspondente à célula.
#### Retorno:

True se o número puder ser colocado na célula, False caso contrário.
### imprimir_tabuleiro(tabuleiro)
Exibe o tabuleiro de Sudoku em um formato amigável ao usuário.

```py
def imprimir_tabuleiro(tabuleiro):
    print("   1 2 3   4 5 6   7 8 9 ")
    print("  " + " -" * 12)
    for i, linha in enumerate(tabuleiro):
        print(f"{i+1}|", end=" ")
        for j, valor in enumerate(linha):
            if valor == 0:
                print(". ", end="")
            else:
                print(f"{valor} ", end="")
            if (j + 1) % 3 == 0:
                print("|", end=" ")
        print()
        if (i + 1) % 3 == 0:
            print("  " + " -" * 12)
```

#### Parâmetros:

- tabuleiro: O tabuleiro de Sudoku.
#### Descrição:

- Imprime o tabuleiro 9x9, onde células vazias são representadas por pontos (.).
- As caixas 3x3 são separadas por linhas e colunas.
### esta_resolvido(tabuleiro)
Verifica se o tabuleiro foi completamente resolvido.
```py
def esta_resolvido(tabuleiro):
    # Verifica se não há células vazias
    for linha in range(9):
        for coluna in range(9):
            if tabuleiro[linha][coluna] == 0:
                return False

    # Verifica se todas as linhas, colunas e caixas 3x3 contêm números únicos de 1 a 9
    for i in range(9):
        if not linha_valida(tabuleiro, i) or not coluna_valida(tabuleiro, i) or not caixa_valida(tabuleiro, i // 3 * 3, i % 3 * 3):
            return False

    return True
```

#### Parâmetros:

tabuleiro: O tabuleiro de Sudoku.
#### Descrição:

Verifica se todas as células estão preenchidas e se todas as linhas, colunas e caixas 3x3 contêm números de 1 a 9 sem repetições.
#### Retorno:

True se o tabuleiro está completamente resolvido, False caso contrário.
### linha_valida(tabuleiro, linha)
Verifica se uma linha contém números válidos de 1 a 9.
```py
def linha_valida(tabuleiro, linha):
    return len(set(tabuleiro[linha])) == 9
```

#### Parâmetros:

- tabuleiro: O tabuleiro de Sudoku.
- linha: O índice da linha a ser verificada.
#### Retorno:

True se a linha contém números únicos, False caso contrário.
### coluna_valida(tabuleiro, coluna)
Verifica se uma coluna contém números válidos de 1 a 9.
```py
def coluna_valida(tabuleiro, coluna):
    return len(set(tabuleiro[i][coluna] for i in range(9))) == 9
```

#### Parâmetros:

- tabuleiro: O tabuleiro de Sudoku.
- coluna: O índice da coluna a ser verificada.
#### Retorno:

True se a coluna contém números únicos, False caso contrário.
### caixa_valida(tabuleiro, inicio_linha, inicio_coluna)
Verifica se uma caixa 3x3 contém números válidos de 1 a 9.
```py
def caixa_valida(tabuleiro, inicio_linha, inicio_coluna):
    caixa = [tabuleiro[i][j] for i in range(inicio_linha, inicio_linha + 3) for j in range(inicio_coluna, inicio_coluna + 3)]
    return len(set(caixa)) == 9
```

#### Parâmetros:

- tabuleiro: O tabuleiro de Sudoku.
- inicio_linha: A linha inicial da caixa 3x3.
- inicio_coluna: A coluna inicial da caixa 3x3.
#### Retorno:

True se a caixa contém números únicos, False caso contrário.
### jogar_sudoku(tabuleiro)
Permite que o jogador interaja com o tabuleiro e jogue o Sudoku.
```py
def jogar_sudoku(tabuleiro):
    while not esta_resolvido(tabuleiro):
        imprimir_tabuleiro(tabuleiro)
        print("Digite 'q' para desistir e ver a solução.")
        entrada_linha = input("Digite a linha (1-9): ")
        if entrada_linha == 'q':
            print("Aqui está a solução:")
            if resolver_sudoku(tabuleiro):
                imprimir_tabuleiro(tabuleiro)
            return
        linha = int(entrada_linha) - 1
        coluna = int(input("Digite a coluna (1-9): ")) - 1
        if tabuleiro[linha][coluna] != 0:
            print("Esta célula já está preenchida. Escolha outra.")
            continue
        num = int(input("Digite um número (1-9): "))
        if not movimento_valido(tabuleiro, linha, coluna, num):
            print("Movimento inválido! Tente novamente.")
            continue
        tabuleiro[linha][coluna] = num
    print("Parabéns! Você resolveu o Sudoku!")
    imprimir_tabuleiro(tabuleiro)
```

#### Parâmetros:

tabuleiro: O tabuleiro de Sudoku parcialmente preenchido.
#### Descrição:

- O jogador insere a linha, a coluna e o número para tentar preencher o tabuleiro.
- O jogo verifica se a célula está vazia e se o movimento é válido.
- O jogador pode digitar 'q' para desistir e ver a solução automática do quebra-cabeça.
- O jogo continua até que o tabuleiro seja resolvido.
#### Retorno:

A função imprime o tabuleiro resolvido quando o jogador vence ou desiste.
