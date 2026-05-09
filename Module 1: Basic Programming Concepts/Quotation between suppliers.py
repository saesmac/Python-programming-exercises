def comparar_cotacoes(cotacao1, cotacao2):
    if cotacao1 < cotacao2:
        print("A cotação do fornecedor 1 é mais barata.")
    elif cotacao1 > cotacao2:
        print("A cotação do fornecedor 2 é mais barata.")
    else:
        print("As cotações dos dois fornecedores são iguais.") 
cotacao1 = float(input("Digite a cotação do fornecedor 1: "))
cotacao2 = float(input("Digite a cotação do fornecedor 2: "))
comparar_cotacoes(cotacao1, cotacao2)