import random


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

def encontrar_celula_vazia(tabuleiro):
    for linha in range(9):
        for coluna in range(9):
            if tabuleiro[linha][coluna] == 0:
                return linha, coluna
    return -1, -1  # Se não houver mais células vazias, retorne -1

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

def linha_valida(tabuleiro, linha):
    return len(set(tabuleiro[linha])) == 9

def coluna_valida(tabuleiro, coluna):
    return len(set(tabuleiro[i][coluna] for i in range(9))) == 9

def caixa_valida(tabuleiro, inicio_linha, inicio_coluna):
    caixa = [tabuleiro[i][j] for i in range(inicio_linha, inicio_linha + 3) for j in range(inicio_coluna, inicio_coluna + 3)]
    return len(set(caixa)) == 9

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

# Gera um quebra-cabeça Sudoku
tabuleiro = gerar_sudoku()
# Joga o jogo Sudoku
jogar_sudoku(tabuleiro)
