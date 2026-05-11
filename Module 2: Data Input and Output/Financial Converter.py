def conversor():
    Real = float(input("Digite o valor em Real: "))
    Cotação = float(input("Digite a cotação do dólar: "))
    Dolar = Real / Cotação
    print(f"O valor em Dólar é: {Dolar:.2f}")
conversor()