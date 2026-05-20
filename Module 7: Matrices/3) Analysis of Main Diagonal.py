# Entrada da matriz 3x3
matriz = []
print("Digite os valores da matriz 3x3:")
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Valor para posição [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

# Extrair diagonal principal
diagonal = [matriz[i][i] for i in range(3)]
soma = sum(diagonal)

# Saída esperada
print("\n===== RELATÓRIO DIAGONAL PRINCIPAL =====")
print(f"Diagonal {diagonal} Soma {soma}")
print("========================================")
