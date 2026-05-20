def main():
    # Entrada da matriz 3x3
    matriz = []
    print("Digite os valores da matriz 3x3:")
    for i in range(3):
        linha = []
        for j in range(3):
            valor = int(input(f"Valor para posição [{i}][{j}]: "))
            linha.append(valor)
        matriz.append(linha)

    # Relatório por linha / prateleira 
    print("\n===== RELATÓRIO DE ESTOQUE =====")
    for i in range(3):
        soma_linha = sum(matriz[i])
        print(f"Linha {i} = {soma_linha}", end=" | ")
        soma_coluna = sum(matriz[j][i] for j in range(3))
        print(f"Coluna {i} = {soma_coluna}")
    print("================================")

if __name__ == "__main__":
    main()
