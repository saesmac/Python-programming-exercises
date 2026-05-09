Odometro_antes = float(input("Digite o valor do odômetro antes da viagem: "))
Odometro_depois = float(input("Digite o valor do odômetro depois da viagem: "))
Combustivel_gasto = float(input("Digite a quantidade de combustível gasto na viagem: "))
Valor_litro = float(input("Digite o valor do litro de combustível: "))
Distancia_percorrida = Odometro_depois - Odometro_antes
Consumo_medio = Distancia_percorrida / Combustivel_gasto
Custo_total = Combustivel_gasto * Valor_litro
print(f"O consumo médio do veículo é: {Consumo_medio:.2f} km/l")
print(f"O custo total da viagem é: {Custo_total:.2f} reais")