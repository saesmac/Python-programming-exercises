Valor = float(input('Digite o valor da compra: '))
if Valor <= 100:
    desconto = 0
elif Valor < 300:
    desconto = 0.05
elif Valor > 301:
    desconto = 0.1
Valor_desconto = Valor * desconto
Valor_final = Valor - Valor_desconto
print(f'Valor do desconto: R${Valor_desconto:.2f} |Valor final a pagar: R${Valor_final:.2f}')