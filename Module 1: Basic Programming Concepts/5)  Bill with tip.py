Valor_compra = float(input("Digite o valor da compra: "))
Valor_taxa = float(input('Digite a porcentagem da taxa (ex: 10 para 10%): '))
Valor_total = Valor_compra + (Valor_compra * (Valor_taxa / 100))
print(f'O valor total da compra, incluindo a taxa, é: R${Valor_total:.2f}')