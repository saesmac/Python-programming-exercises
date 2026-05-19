total= 0 #acumulador para o total da fatura
pedidos_quantidade = int(input("Digite a quantidade de pedidos: "))
for i in range(1, pedidos_quantidade + 1):
    preco = float(input(f"Digite o preço do pedido {i}: "))
    total += preco #acumula o preço do pedido no total
media = total / pedidos_quantidade #calcula a média dos pedidos
print(f"O total da fatura é: R${total:.2f}| A média dos pedidos é: R${media:.2f}")