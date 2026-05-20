#controle de estoque específico
#Código alvo
cdg_alvo = input("Digite o código do produto a ser verificado: ")
total_vendido = 0
while True:
    #Entrada de transações
    cdg = int(input("Digite o código da transação (ou 0 para encerrar): "))
    if cdg == 0:
        break
    qtd = int(input("Digite a quantidade vendida: "))

    #se for o código alvo, acumula a quantidade vendida
    if cdg == int(cdg_alvo):
        total_vendido += qtd

#Resultado final
print(f'\n=== Relatório de Estoque ===')
print(f"\nTotal vendido do produto {cdg_alvo}: {total_vendido} unidades.")