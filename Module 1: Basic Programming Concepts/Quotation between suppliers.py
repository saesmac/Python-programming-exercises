def comparar_cotacoes(cotacao1, cotacao2):
    if cotacao1 < cotacao2:
        print(f"A cotação do fornecedor 1 é mais barata: R${cotacao1:.2f}")
    elif cotacao1 > cotacao2:
        print(f"A cotação do fornecedor 2 é mais barata: R${cotacao2:.2f}")
    else:
        print("As cotações dos dois fornecedores são iguais.") 
cotacao1 = float(input("Digite a cotação do fornecedor 1: "))
cotacao2 = float(input("Digite a cotação do fornecedor 2: "))
comparar_cotacoes(cotacao1, cotacao2)