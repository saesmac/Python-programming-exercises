# Simulação de conta de energia com interação

tarifa_reduzida = 0.50   # até 100 kWh
tarifa_normal = 0.70     # acima de 100 kWh
taxa_fixa = 30.00        # taxa fixa mensal

print("=== Simulador de Conta de Energia ===")
N = int(input("Quantos meses deseja simular? "))

contas = []

for mes in range(1, N+1):
    print(f"\n--- Mês {mes} ---")
    consumo = float(input("Digite o consumo em kWh: "))
    
    if consumo <= 100:
        valor = consumo * tarifa_reduzida + taxa_fixa
        print(f"Faixa aplicada: até 100 kWh (R$ {tarifa_reduzida:.2f}/kWh)")
    else:
        valor = consumo * tarifa_normal + taxa_fixa
        print(f"Faixa aplicada: acima de 100 kWh (R$ {tarifa_normal:.2f}/kWh)")
    
    print(f"Taxa fixa: R$ {taxa_fixa:.2f}")
    print(f"Conta do mês {mes}: R$ {valor:.2f}")
    
    contas.append(valor)

# Resumo final
print("\n=== Resumo Final ===")
for i, valor in enumerate(contas, start=1):
    print(f"Mês {i}: R$ {valor:.2f}")

media = sum(contas) / N
print(f"\nMédia mensal da conta: R$ {media:.2f}")
print("Obrigado por usar o simulador! ⚡")
