# Tabuleiro Dinâmico - Jogo da Velha com validação de entrada

# Inicializa tabuleiro 3x3 vazio
tabuleiro = [[" " for _ in range(3)] for _ in range(3)]

def mostrar_tabuleiro(tab):
    print("\n")
    for i, linha in enumerate(tab):
        print(" | ".join(linha))
        if i < 2:
            print("--+---+--")
    print("\n")

def ha_espacos_vazios(tab):
    return any(" " in linha for linha in tab)

def verificar_vitoria(tab, simbolo):
    # Linhas
    for linha in tab:
        if all(casa == simbolo for casa in linha):
            return True
    # Colunas
    for col in range(3):
        if all(tab[linha][col] == simbolo for linha in range(3)):
            return True
    # Diagonal principal
    if all(tab[i][i] == simbolo for i in range(3)):
        return True
    # Diagonal secundária
    if all(tab[i][2-i] == simbolo for i in range(3)):
        return True
    return False

jogador_atual = "X"
while True:
    mostrar_tabuleiro(tabuleiro)
    print(f"Vez do jogador {jogador_atual}")

    try:
        linha = int(input("Linha (0-2): "))
        coluna = int(input("Coluna (0-2): "))
    except ValueError:
        print("⚠️ Entrada inválida! Digite números entre 0 e 2.")
        continue

    # Verifica se está dentro do intervalo
    if linha not in [0,1,2] or coluna not in [0,1,2]:
        print("⚠️ Linha ou coluna inválida! Digite valores entre 0 e 2.")
        continue

    simbolo = jogador_atual

    # Verifica se a posição está livre
    if tabuleiro[linha][coluna] == " ":
        tabuleiro[linha][coluna] = simbolo
    else:
        print("⚠️ Essa posição já está ocupada, tente outra.")
        continue

    # Verifica vitória
    if verificar_vitoria(tabuleiro, jogador_atual):
        mostrar_tabuleiro(tabuleiro)
        print(f"🎉 Jogador {jogador_atual} venceu!")
        break

    # Verifica empate
    if not ha_espacos_vazios(tabuleiro):
        mostrar_tabuleiro(tabuleiro)
        print("🤝 Empate! Não há mais espaços vazios.")
        break

    # Alterna jogador
    jogador_atual = "O" if jogador_atual == "X" else "X"
