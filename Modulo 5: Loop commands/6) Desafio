# Pesquisa de Satisfação

soma_idades = 0
soma_notas = 0
qtd_respostas = 0
promotores = 0  # notas 4 ou 5

while True:
    idade = int(input("Digite a idade (0 para encerrar): "))
    if idade == 0:
        break
    nota = int(input("Digite a nota (1 a 5): "))

    soma_idades += idade
    soma_notas += nota
    qtd_respostas += 1

    if nota >= 4:
        promotores += 1

# Evitar divisão por zero
if qtd_respostas > 0:
    idade_media = soma_idades / qtd_respostas
    nota_media = soma_notas / qtd_respostas
    print("\n=== Resultado da Pesquisa ===")
    print(f"Idade média: {idade_media:.1f}")
    print(f"Nota média: {nota_media:.2f}")
    print(f"Quantidade de promotores: {promotores}")
else:
    print("Nenhuma resposta registrada.")
