# Transposição de matriz com entrada do usuário

# Lê dimensões da matriz
linhas = int(input("Digite o número de linhas da matriz: "))
colunas = int(input("Digite o número de colunas da matriz: "))

# Lê os elementos da matriz
matriz = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f"Digite o elemento [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

# Cria matriz transposta (colunas viram linhas)
transposta = [[0 for _ in range(linhas)] for _ in range(colunas)]

for i in range(linhas):
    for j in range(colunas):
        transposta[j][i] = matriz[i][j]

# Exibe resultados
print("\nMatriz original:")
for linha in matriz:
    print(linha)

print("\nMatriz transposta:")
for linha in transposta:
    print(linha)
