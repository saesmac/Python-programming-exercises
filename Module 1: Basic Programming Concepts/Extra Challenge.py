Nome_produto = input("Digite o nome do produto: ")
preco_produto = float(input("Digite o preço do produto: "))
quantidade_produto = int(input("Digite a quantidade do produto: "))
total = preco_produto * quantidade_produto
Taxa_servico = total * 0.1
total_com_taxa = total + Taxa_servico
print(f"O total a pagar pelo produto {Nome_produto} é: R${total_com_taxa:.2f}")