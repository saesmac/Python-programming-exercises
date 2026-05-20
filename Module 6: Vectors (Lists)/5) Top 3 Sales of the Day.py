#Entrada de vendas
entrada = input("Digite as vendas do dia (separadas por espaço): ")
#converte a entrada em uma lista de números
vendas = [float(x) for x in entrada.split()]
#ordena as vendas em ordem decrescente
vendas.sort(reverse=True)
#exibe as 3 maiores vendas
print("\n=== Top 3 Vendas do Dia ===")
for i in range(min(3, len(vendas))):
    print(f"{i+1}º lugar: R${vendas[i]:.2f}")