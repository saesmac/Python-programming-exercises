precos = []

# Entrada do ajuste
ajuste_input = input("Digite o valor de ajuste (ex: R$10 ou 10% ou -10%): ").strip()

# Verifica se é percentual ou valor em reais
if ajuste_input.endswith('%'):
    # Percentual (positivo ou negativo)
    ajuste_percentual = float(ajuste_input.replace('%', '').replace(',', '.')) / 100
    tipo_ajuste = 'percentual'
else:
    # Valor fixo em reais (positivo ou negativo)
    ajuste_valor = float(ajuste_input.replace('R$', '').replace(',', '.'))
    tipo_ajuste = 'valor'

# Entrada dos preços
while True:
    preco_input = input("Digite um preço (ou 'sair' para encerrar): ")
    if preco_input.lower() == 'sair':
        break
    try:
        preco = float(preco_input.replace('R$', '').replace(',', '.'))
        precos.append(preco)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número ou 'sair'.")

# Aplicando reajuste
if tipo_ajuste == 'percentual':
    precos_ajustados = [preco * (1 + ajuste_percentual) for preco in precos]
else:
    precos_ajustados = [preco + ajuste_valor for preco in precos]

# Exibindo resultados
print("\n=== Preços Ajustados ===")
for i, preco_ajustado in enumerate(precos_ajustados):
    print(f"Preço original: R${precos[i]:.2f} -> Preço ajustado: R${preco_ajustado:.2f}")
