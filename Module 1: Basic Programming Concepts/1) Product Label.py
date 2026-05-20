Nome_produto = input("Digite o nome do produto: ")
Preco_produto = float(input("Digite o preço do produto: "))
Quantidade = int(input("Digite a quantidade do produto: "))
Valor_total = Preco_produto * Quantidade
print(f"O valor total da compra de {Quantidade} unidades do produto {Nome_produto} é: R${Valor_total:.2f}")
